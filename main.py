import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta

def get_downloads_path():
    """
    Obtém o caminho da pasta Downloads do usuário atual, independente do SO.
    """
    return str(Path.home() / "Downloads")

def create_station_directories():
    """
    Cria as pastas padrão para cada estação na pasta Downloads do usuário.
    """
    base_path = Path(get_downloads_path()) / "hidro-telemetria-data"
    
    stations = {
        "jiparana": "15560000",
        "ariquemes": "15430000", 
        "portovelho": "15400000",
        "guajara": "15250000"
    }
    
    station_dict = {}
    
    for station_name, code in stations.items():
        station_dir = base_path / station_name.capitalize()
        station_dir.mkdir(parents=True, exist_ok=True)
        
        station_dict[station_name] = {
            "code": code,
            "directory": str(station_dir)
        }
        
        print(f"📁 Pasta criada/verificada: {station_dir}")
    
    return station_dict

# Criar diretórios e configurar dicionário de estações
print("🔧 Configurando pastas de download...")
stationCodeDict = create_station_directories()
print("✅ Configuração concluída!\n")

driver = None

def startAutomation(directoryPath, stationCode):
    global driver
    
    # Verificar se o diretório existe e criar se necessário
    if not os.path.exists(directoryPath):
        os.makedirs(directoryPath, exist_ok=True)
        print(f"📁 Pasta criada: {directoryPath}")

    # Configure Chrome options
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": directoryPath,        # Set download folder
        "download.prompt_for_download": False,             # Disable "Save As" prompt
        "plugins.always_open_pdf_externally": True,        # Download PDF instead of opening in browser
    }
    chrome_options.add_experimental_option("prefs", prefs)    # Setup the Chrome WebDriver service using automatic driver management
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)

    # Open the target website
    driver.get("https://www.snirh.gov.br/hidrotelemetria")
    
    
    # Main workflow
    # Navigate to the station filter page
    goToStationFilter()

    # Apply the station filter for "portovelho"
    filterStation(stationCode)

    # Apply the date filter
    filterDate()

    # Download File
    clickTodownload()

    # Wait for 10 seconds to allow results to load
    time.sleep(10)

    # Close the browser
    driver.quit()

def goToStationFilter():
    """
    Navigates to the station filter page by interacting with the menu system.
    """
    # Wait until the "Acesso ao Mapa" button is available and click it
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Acesso ao Mapa"))
    )
    AcessoMapaBtn = driver.find_element(By.LINK_TEXT, "Acesso ao Mapa")
    AcessoMapaBtn.click()

    # Wait until "Visualizar Dados" menu is available and hover over it
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//li[@class='has-popup static' and @aria-haspopup='Menu1:submenu:7']//a"))
    )
    visualizarDadosMenu = driver.find_element(By.XPATH, "//li[@class='has-popup static' and @aria-haspopup='Menu1:submenu:7']//a")
    actions = ActionChains(driver)
    actions.move_to_element(visualizarDadosMenu).perform()

    # Wait until "Serie Historica" option is available and click it
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='Menu1']//ul[@id='Menu1:submenu:7']//a[@href='serieHistorica.aspx']"))
    )
    serieHistorica = driver.find_element(By.XPATH, "//div[@id='Menu1']//ul[@id='Menu1:submenu:7']//a[@href='serieHistorica.aspx']")
    serieHistorica.click()

def filterStation(stationCode):
    """
    Filters the station by entering the station code and selecting the first result.

    Args:
        stationCode (str): The code of the station to filter.
    """
    # Wait until the station search input is available
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "cphCorpo_ctl01_txtPesquisa"))
    )

    # Enter the station code into the search box and press ENTER
    input_station = driver.find_element(By.ID, "cphCorpo_ctl01_txtPesquisa")
    input_station.clear()
    input_station.send_keys(stationCode + Keys.ENTER)

    # Wait for the station dropdown to load
    time.sleep(5)  # Optional: Adjust based on actual load time
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "cphCorpo_ctl01_lstEstacoes"))
    )

    # Select the first station from the dropdown
    dropdownStation = driver.find_element(By.ID, "cphCorpo_ctl01_lstEstacoes")
    select = Select(dropdownStation)
    select.select_by_index(0)

def filterDate():
    """
    Filters data by setting the date range to yesterday and today.
    """
    presentDay = datetime.now()
    yesterday = presentDay - timedelta(1)

    # Wait until the date filter input is available
    time.sleep(5)  # Optional: Adjust based on actual load time
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "cphCorpo_ctl01_txtPeriodoDe"))
    )

    # Input the date range and trigger the filter
    input_date = driver.find_element(By.ID, "cphCorpo_ctl01_txtPeriodoDe")
    input_date.clear()
    input_date.send_keys(
        yesterday.strftime('%d/%m/%Y') + Keys.TAB + "00:00" + Keys.TAB + \
        presentDay.strftime('%d/%m/%Y') + Keys.TAB + "08:00" + Keys.TAB + Keys.ENTER
    )

def clickTodownload():
    time.sleep(5)
    
    # Wait until element exist
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "cphCorpo_btExportar"))
    )

    # Click on link
    link = driver.find_element(By.ID, "cphCorpo_btExportar")
    link.click()

def runAllStations():
    """
    Executa a automação para todas as estações configuradas no dicionário.
    """
    print("Iniciando automação para todas as estações...")
    
    for station_name, station_info in stationCodeDict.items():
        print(f"\nProcessando estação: {station_name.upper()}")
        print(f"Código: {station_info['code']}")
        print(f"Diretório: {station_info['directory']}")
        
        try:
            startAutomation(station_info["directory"], station_info["code"])
            print(f"✅ Download concluído para {station_name.upper()}")
        except Exception as e:
            print(f"❌ Erro ao processar {station_name.upper()}: {str(e)}")
        
        # Aguardar um pouco entre as execuções para evitar sobrecarga
        time.sleep(2)
    
    print("\n🎉 Automação concluída para todas as estações!")

# Executar para todas as estações
runAllStations()