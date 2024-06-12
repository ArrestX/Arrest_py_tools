import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
import re
from fake_useragent import UserAgent

def aizhan_chaxun(ip):
    ua = UserAgent().random
    headers = {
        'User-Agent': ua,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://dns.aizhan.com/'
    }
    aizhan_url = f'https://dns.aizhan.com/{ip}/'
    try:
        response = requests.get(aizhan_url, headers=headers, timeout=5)
        domains = re.findall(r'''rel="nofollow" target="_blank">(.*?)</a>''', response.text)
        return domains
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return []

def ip138_chaxun(ip):
    ua = UserAgent().random
    headers = {
        'Host': 'site.ip138.com',
        'User-Agent': ua,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://site.ip138.com/'
    }
    ip138_url = f'https://site.ip138.com/{ip}/'
    try:
        response = requests.get(ip138_url, headers=headers, timeout=5)
        domains = re.findall(r'''<a href="/domain/(.*?)/" target="_blank">''', response.text)
        return domains
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return []

def query_domains():
    ips = ip_entry.get("1.0", tk.END).strip()
    result_text.delete('1.0', tk.END)
    if not ips:
        messagebox.showinfo("Info", "Please enter at least one IP address.")
        return
    ip_list = re.split(r'[\n,]+', ips)
    for ip in ip_list:
        if ip.strip():
            aizhan_domains = aizhan_chaxun(ip.strip())
            ip138_domains = ip138_chaxun(ip.strip())
            result_text.insert(tk.END, f"IP: {ip}\nAizhan Domains:\n")
            if aizhan_domains:
                result_text.insert(tk.END, "\n".join(aizhan_domains) + "\n\n")
            else:
                result_text.insert(tk.END, "No domains found on Aizhan.\n\n")
            result_text.insert(tk.END, f"IP138 Domains:\n")
            if ip138_domains:
                result_text.insert(tk.END, "\n".join(ip138_domains) + "\n\n")
            else:
                result_text.insert(tk.END, "No domains found on IP138.\n\n")

def extract_ips():
    raw_data = input_text.get("1.0", tk.END).strip()
    ip_pattern = r'http://(\d+\.\d+\.\d+\.\d+)(?::\d+)?'
    ips = set(re.findall(ip_pattern, raw_data))
    output_text.delete('1.0', tk.END)
    for ip in sorted(ips):
        output_text.insert(tk.END, ip + '\n')

app = tk.Tk()
app.title("IP Tools by Arrest")

# Layout configuration
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Domain Query section
domain_query_label = ttk.Label(app, text="Enter IP Addresses for Domain Query (separate by newline or comma):")
domain_query_label.grid(row=0, column=0, padx=5, pady=5, sticky='nw')
ip_entry = scrolledtext.ScrolledText(app, height=10, width=50)
ip_entry.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
query_button = ttk.Button(app, text="Query Domains", command=query_domains)
query_button.grid(row=2, column=0, padx=5, pady=5, sticky='ew')
result_text = scrolledtext.ScrolledText(app, height=10, width=50)
result_text.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

# IP Extraction section
extraction_label = ttk.Label(app, text="Enter Raw Data for IP Extraction:")
extraction_label.grid(row=0, column=1, padx=5, pady=5, sticky='nw')
input_text = scrolledtext.ScrolledText(app, height=10, width=50)
input_text.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')
extract_button = ttk.Button(app, text="Extract IPs", command=extract_ips)
extract_button.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
output_text = scrolledtext.ScrolledText(app, height=10, width=50)
output_text.grid(row=3, column=1, padx=5, pady=5, sticky='nsew')

app.mainloop()