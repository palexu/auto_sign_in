import sys
import time
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver

class yishuwang:
    def __init__(self):
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")

    def login(self):
        self.driver.get("https://kindbook.cn/plugin.php?id=jz52_dl:index")
        u = self.driver.find_element_by_xpath('//*[@id="ls_username"]')
        u.clear()
        u.send_keys("palexu")
        p=self.driver.find_element_by_xpath('//*[@id="ls_password"]')
        p.clear()
        p.send_keys("xujunyu520")
        login_b=self.driver.find_element_by_xpath('//*[@id="lsform"]/table/tbody/tr[3]/td[2]/button')
        login_b.click()

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

            self.msg()
        except Exception as e:
            self.msg("益书网签到异常",str(e))
        finally:
            self.driver.quit()

    def msg(self,title="益书网签到成功",message=""):
        scKey='SCU11255T9aac1a1f33b21e14d151caa16d6b424d59a66f9a1264f'
        requests.get("https://sc.ftqq.com/" + scKey + ".send?text=" + title + "&desp=" + message)

def run():
    try:
        y = yishuwang()
        y.login()
        y.sign_in()
    except Exception as e:
        print(e)
    finally:
        y.driver.quit()

if __name__ == '__main__':
    sched = BlockingScheduler()
    sched.add_job(run, 'cron', hour="7")
    try:
        sched.start()
    except KeyboardInterrupt:
        pass







