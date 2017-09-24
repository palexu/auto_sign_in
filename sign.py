import sys
import time
import requests
import yaml
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver

class yishuwang:
    def __init__(self):
        with open("config.yml") as f:
            config = yaml.load(f)
        driver_type = config["driver"].lower()
        if "chrome" == driver_type:
            self.driver = webdriver.Chrome(config["path"])
        elif "phantomjs" == driver_type:
            cap = webdriver.DesiredCapabilities.PHANTOMJS
            cap["phantomjs.page.settings.resourceTimeout"] = 1000
            cap["phantomjs.page.settings.loadImages"] = False
            cap["phantomjs.page.settings.disk-cache"] = True
            self.driver = webdriver.PhantomJS(executable_path=config["path"],desired_capabilities=cap)
        else:
            print("sorry,we does not support driver except Chrome and PhantomJS....")
            return
        print("browser open success")
        self.username = config["username"]
        self.password = config["password"]
        self.scKey = config["scKey"]
        self.devMode = True

    def login(self):
        try:
            self.driver.get("https://kindbook.cn/plugin.php?id=jz52_dl:index")
            u = self.driver.find_element_by_xpath('//*[@id="ls_username"]')
            u.clear()
            u.send_keys(self.username)
            p=self.driver.find_element_by_xpath('//*[@id="ls_password"]')
            p.clear()
            p.send_keys(self.password)
            login_b=self.driver.find_element_by_xpath('//*[@id="lsform"]/table/tbody/tr[3]/td[2]/button')
            login_b.click()
        except Exception as e:
            if not self.devMode:
                self.msg("益书网签到异常",str(e))
            print(e)

    def sign_in(self):
        try:
            time.sleep(3)
            check_in_b = self.driver.find_element_by_xpath('//*[@id="mn_N462e"]/a')
            check_in_b.click()

            #切换到签到的页面
            windows = self.driver.window_handles
            for i in windows:
                if i!=self.driver.current_window_handle:
                    self.driver.switch_to_window(i)

            #选择表情
            time.sleep(3)
            biaoqing = self.driver.find_element_by_xpath('//*[@id="kx_s"]')
            biaoqing.click()

            #提交
            do_check_in_b = self.driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div[1]/form/table/tbody/tr/td/div/input')
            do_check_in_b.click()

            if not self.devMode:
                self.msg()
        except Exception as e:
            if not self.devMode:
                self.msg("益书网签到异常",str(e))
            print(e)
        finally:
            self.driver.quit()

    def msg(self,title="益书网签到成功",message=""):
        requests.get("https://sc.ftqq.com/" + self.scKey + ".send?text=" + title + "&desp=" + message)

def run():
    try:
        y = yishuwang()
        y.login()
        # y.sign_in()
    except Exception as e:
        print(e)
    finally:
        y.driver.quit()

if __name__ == '__main__':
    run()
    
    # sched = BlockingScheduler()
    # sched.add_job(run, 'cron', hour="7")
    # try:
    #     print("job start")
    #     sched.start()
    # except KeyboardInterrupt:
    #     pass







