from playwright.sync_api import sync_playwright

def take_screenshot():
    with sync_playwright() as p:
        # 启动 Chromium
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 800}) # 根据需要调整视口大小
        
        # 访问目标网页
        page.goto('https://sensor.cns.ac.cn', wait_until='networkidle')
        
        # 截图并保存到 Jekyll 的图片目录 (假设路径是 assets/images)
        page.screenshot(path='assets/images/sensor-preview.png')
        
        browser.close()

if __name__ == '__main__':
    take_screenshot()