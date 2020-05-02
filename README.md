[English Readme](README_EN.md)

dragonpilot (龍芯駕駛輔助系統)
---
龍芯駕駛輔助系統是一套基於 [openpilot](https://github.com/commaai/openpilot/) 的開源 L2 級自動駕駛系統軟體，它可以升級您車子裡的 ACC (主動式定速巡航系統) 以及 LKAS (車道保持輔助系統) 至接近特斯拉 Autopilot 的等級。 

龍芯駕駛輔助系統在 openpilot 的基礎上加入更多客制化的功能，目前有：

* 多語言介面 (目前支援：英文、简体、繁體，部分支援：日文、韓文、法文、葡萄牙語)
* 不間斷行車記錄
* 可設定的行車介面
* 斷電自動關機 (C2 不適用)
* 轉向燈/方向燈暫時取消控制
* 停止 AI 訓練記錄
* 取消 AI 訓練記錄上傳
* 允許油門：dp 控制時可踩油門
* Noctua 風扇模式
* 完全取消駕駛監控 (人臉+方向盤)
* ACC 模式：讓 dp 只操控油門/剎車
* TOM TOM 測速照相 / 高德地圖 / 神盾測速照相 / 位智 (Waze)
* MiXplorer 檔案管理器
* 側邊欄顯示無線網路 IP 位置
* TOM TOM 測速照相 / 高德地圖使用 / 神盾測速照相 / 位智 (Waze) 使用 Grey Panda / Harness GPS 數據
* 自動換道
* 開機啟動個人熱點
* 不同的加速模式 (只支援由 dp 控制車速的車種，Toyota 需拔 DSU，感謝 @arne182 提供相關代碼)
* 動態調整車距 (只支援由 dp 控制車速的車種，Toyota 需拔 DSU，感謝 @ShaneSmiskol 提供相關代碼)

**更多客制化內容請參閱 [CHANGELOG.md](CHANGELOG.md)**

支援車款
---
除了官方支援的車款外，dp (0.6.4+) 還支援以下車款：
* 大陸版東風本田 Inspire 混動 by KT
* 大陸版本田雅閣混動 
* 大陆版 2018 Toyota Camry 2.0 by Rming
* 大陆版 2018 Toyota Highlander by toyboxZ
* 大陸版 2018 Toyota Camry by 笨木匠
* 大陸版 2020 Toyota RAV4 by 笨木匠
* 大陸版 2019 Toyota 雷凌 (汽油版) by Shell
* 大陸版 2019 Lexus RX300 by cafe
* 大陸版 2019 Toyota 卡羅拉 (汽油版) by Shell
* 台灣版 2016 Toyota Prius by Philip
* 台灣版 201? Toyota RAV4 4WD 5th Gen by Philip
* 台灣版 2020 Toyota Auris w/ LTA by Philip
* 台灣版 2017 Lexus IS200t by Philip / Cody Dai
* 台灣版 2019 Toyota RAV4 Hybrid by MaxDuan
* 台灣版 2019 Toyota RAV4 by MaxDuan / CloudJ
* 台灣版 2019 Toyota Corolla Altis by wlee72
* 台灣版 Lexus CT200h by CloudJ
* 台灣版 Toyota Prius 4.5 代 by Lin Xin Hong
* 台灣版 2017 Lexus GS450h by 簡銘佑
* 波蘭版 2015 Lexus NX200T by wabes

目前完整支援 dragonpilot 客制化功能的車系有：
* Lexus / Toyota
* Honda
* Hyundai
(其它 openpilot 支援的車系仍可使用 dragonpilot 部分的功能。)

畫面截圖
---
![](dp_1.png) ![](dp_2.png) ![](dp_3.png) ![](dp_4.png) ![](dp_5.png) ![](dp_6.png)

**更多請看 screenshots/ 資料夾**

影片
---
<table>
  <tr>
    <td><a href="https://www.youtube.com/watch?v=-Womm0aO8Cc" title="YouTube" rel="noopener"><img src="http://i3.ytimg.com/vi/-Womm0aO8Cc/hqdefault.jpg"></a></td>
    <td><a href="https://www.youtube.com/watch?v=ACrHqodnhKI" title="YouTube" rel="noopener"><img src="http://i3.ytimg.com/vi/ACrHqodnhKI/hqdefault.jpg"></a></td>
    <td><a href="https://www.youtube.com/watch?v=D5M5qci5wsw" title="YouTube" rel="noopener"><img src="http://i3.ytimg.com/vi/D5M5qci5wsw/hqdefault.jpg"></a></td>
    <td><a href="https://www.youtube.com/watch?v=fb0KEZgqH1Y" title="YouTube" rel="noopener"><img src="http://i3.ytimg.com/vi/fb0KEZgqH1Y/hqdefault.jpg"></a></td>
  </tr>
</table>

硬體需求
---
* 一加 oneplus 3t 或者 樂視 LeEco Le Pro3 (x727) 手機 / EON
* Panda
* Giraffe
* 適配的車款


硬件購買
---
您可以至以下的渠道購買相關硬件 (EON / Panda / Giraffe)：

* [comma ai 官方](https://comma.ai/shop/)
* [Taobao](https://shop442817640.taobao.com/)

**我們並沒有與任何渠道商合作，若有任何問題請直接與他們聯系**


安裝 NEOS
---
待補充


安裝 dragonpilot
---
 
1. SSH 至手機後
2. 切換至 /data/ 資料夾 
    ```bash
    cd /data
    ```
3. 備份舊版的 openpilot
    ```bash
    mv openpilot openpilot_bak
    ```
4. 下載 dragonpilot 開發版並存至 openpilot 資料夾 (2 選 1):
    1. github 
    ```bash
    git clone https://github.com/dragonpilot-community/dragonpilot.git openpilot --branch devel-i18n
    ```
    2. gitee
    ```bash 
    git clone https://gitee.com/dragonpilot-community/dragonpilot.git openpilot --branch devel-i18n
    ```
5. 切換到 openpilot 的資料夾
    ```bash
    cd openpilot
    ```
6. 更新 git 資料庫
    ```bash
    git pull
    ```
7. 切換語系 (預設為英文，不想切換可省略此步驟)
    ```bash
    # 简体
    setprop persist.sys.locale zh-CN && setprop persist.sys.local zh-CN
    ```
    ```bash
    # 繁體
    setprop persist.sys.locale zh-TW && setprop persist.sys.local zh-TW
    ```
8.  重開機
    ```bash
    reboot
    ```

**如果重開機後中文字無法正確顯示，請再重開機一次。**


更新 dragonpilot
---
1. 切換至 /data/openpilot 資料夾 
    ```bash
    cd /data/openpilot/scripts/
    ```
2. 執行更新指令
    ```bash
    ./reset_update.sh
    ```

版本分支介紹
---
* docs: 說明檔
* testing: 搶鮮版 - (英文，基於官方 devel-staging/devel 版 + 客制化功能，可能會有問題、錯誤)
* feature-????: 新功能測試版 - (英文，基於 dp testing 版 + 新功能測試，可能會有問題、錯誤)
* devel-i18n: 開發版 - (多語言版，基於 dp testing 版)
* ?.?.?-i18n: 穩定版 - (多語言版，測試過的 devel-i18n)

**其它沒有說明的分支為測試功能版，非必要請勿使用**
