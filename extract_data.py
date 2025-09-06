# extract_data.py

from bs4 import BeautifulSoup
import pandas as pd

def extract_data_from_html(html_files):
    titles = ['Serial No', 'System Name', 'Department', 'Username', 'Location', 'Block', 'Port Number', 'Computer Name', 'Operating System', 'System Model', 'Service Tag', 'Processor', 'Board', 'Hard Disk Drive', 'Memory', 'Display', 'Monitor Brand', 'Display Size', 'No.of RAM slots']
    df = pd.DataFrame(columns=titles)
    serial_no = 1

    for file_path in html_files:
        name = file_path.split('/')[-1].split('_')
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        computer_name = soup.find('table', class_="reportHeader").find_all('tr')[1].find('td').text.strip()
        os_section = soup.find_all('div', class_='reportSection rsLeft')[0].find('td')
        os = os_section.get_text(separator='\n', strip=True).split('\n')[0]
        system_model_section = soup.find_all('div', class_="reportSection rsRight")[0].find('td')
        system_model = system_model_section.get_text(separator='\n', strip=True).split('\n')[0]
        service_tag_section = soup.find_all('div', class_="reportSection rsRight")[0]
        service_tag = service_tag_section.find('a').text.split(' ')[0] if service_tag_section.find('a') else ''
        processor_section = soup.find_all('div', class_="reportSection rsLeft")[1].find('td')
        processor = processor_section.get_text(separator='\n', strip=True).split('\n')[0]
        board_section = soup.find_all('div', class_="reportSection rsRight")[1].find('td')
        board = ''.join(board_section.get_text(separator='\n', strip=True).split('\n')[0].split(' ')[1:])
        hard_disk_section = soup.find_all('div', class_='reportSection rsLeft')[2].find('td')
        hard_disk = hard_disk_section.get_text(separator='\n', strip=True).split('\n')[0].split(' ')[0] + 'GB'
        memory_section = soup.find_all('div', class_="reportSection rsRight")[2].find('td')
        memory = str(int(memory_section.get_text(separator='\n', strip=True).split('\n')[0].split(' ')[0]) / 1000) + 'GB'
        display_section = soup.find_all('div', class_="reportSection rsRight")[4].find('td')
        display = ' '.join(display_section.get_text(separator='\n', strip=True).split('\n')[0].split(' ')[:3])
        monitor_section = soup.find_all('div', class_="reportSection rsRight")[4].find('td')
        monitor_parts = monitor_section.get_text(separator='\n', strip=True).split('\n')
        monitor = ' '.join(monitor_parts[1].split(' ')[:2]) if len(monitor_parts) >= 2 else ' '
        display_size_parts = monitor_section.get_text(separator='\n', strip=True).split('\n')
        display_size = display_size_parts[1].split(' ')[3][1:5] if len(display_size_parts) >= 2 else ' '
        ram_slots_section = soup.find_all('div', class_="reportSection rsRight")[2].find('td')
        ram_slots = ram_slots_section.get_text(separator='\n', strip=True).count('Slot')

        new_row = {
            'Serial No': serial_no,
            'System Name': name[0],
            'Department': name[1],
            'Username': name[2],
            'Location': name[3],
            'Block': name[4],
            'Port Number': name[5][:-5],
            'Computer Name': computer_name,
            'Operating System': os,
            'System Model': system_model,
            'Service Tag': service_tag,
            'Processor': processor,
            'Board': board,
            'Hard Disk Drive': hard_disk,
            'Memory': memory,
            'Display': display,
            'Monitor Brand': monitor,
            'Display Size': display_size,
            'No.of RAM slots': ram_slots
        }
        df.loc[len(df)] = new_row
        serial_no += 1

    return df
