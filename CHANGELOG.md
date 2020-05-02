dp v0.7.5 (testing / devel-i18n 分支)
========================
* [更新] dp 圖示 (特別感謝 @wabes 的設計與提供)。
* [更新] 中文版整合進 i18n 版。  
* [刪除] 指紋暫存功能。
* [新增] 倒車黑屏功能。
* [新增] 駕駛介面加入「加速模式」切換鈕。 
* [新增] 自定義車型。

2020-04-16
========================
* [DEVEL] 加入台灣版 2016 Lexus IS200t 指紋。(感謝 Philip / Cody Dai)
* [DEVEL] 加入台灣版 2016 Toyota Prius 4.5 代指紋。(感謝 Philip)
* [DEVEL] 加入台灣版 201x Toyota RAV4 4WD 指紋。(感謝 Philip)
* [DEVEL] 加入台灣版 2020 Toyota Auris w/ LTA 指紋。(感謝 Philip)
* [DEVEL] 修正 commIssue 錯誤。(感謝 Kent 協助)

2020-04-13
========================
* [DEVEL] 加入可調整 Toyota Sng 起步反應值 (DragonToyotaSngResponse)。 (特別感謝 @Wei 提供 PR)
* [DEVEL] 駕駛介面加入「動態調整車距」按鈕。(感謝 @cgw1968-5779 建議)
* [DEVEL] 更新 update script。(感謝 深鯨希西 回報)

2020-04-10
========================
* [DEVEL] 更新 panda 至最新的 comma:master 分支。
* [DEVEL] 移除所有的第三方應用改為自動下載。
* [DEVEL] 移除「啟用原廠 DSU 模式」、「安全帶檢查」、「車門檢查」開關。
* [0.7.4] 更新至 2020-04-10 devel 分支。

2020-03-31
========================
* [TESTING] 還原部分修改代碼以達到 comma ai 安全準則。 (Reverted changes to panda safety code to comply with comma ai safety guideline.)
* [TESTING] 調整「啟用原廠 DSU 模式」為踩剎車時會暫時斷開控制 。(Enable Stock DSU Mode will temporary disable controls when brake is pressed.)
* [DEVEL] 更新至 2020-03-31 testing 分支。
* [0.7.4] 更新至 2020-03-31 devel 分支。

2020-03-27
========================
* [DEVEL] 更新至最新的 testing 分支:
  * 加入波蘭版 2015 Lexus NX200T 支援。(感謝 wabes 提供)
  * 調整「啟用原廠 DSU 模式」為不再需要 AHB 。(Enable Stock DSU Mode no longer requires "AHB" toggle)
  * 加入「安全帶檢查」、「車門檢查」、「檔位檢查」、「溫度檢查」開關。
  * 加入曲率學習功能 - Curvature Learner 。(感謝 zorrobyte 提供)
  * 加入大陸版 2018 Toyota Highlander 支援。(感謝 toyboxZ 提供)
  * 加入大陸版 2018 Toyota Camry 2.0 支援。(感謝 Rming 提供)
  * 加入韓文支持。(感謝 crwusiz 提供)
  * 調整 OFFROAD 主頁翻譯將 "dragonpilot" 改回 "openpilot"。

2020-03-22
========================
* [TESTING] 更新至最新的 commaai:devel-staging 和 commaai:devel 分支 (0.7.4)。
* [DEVEL] 更新至最新的 testing 分支。
* [0.7.4] 建立，基於 2020-03-22 DEVEL 分支。

2020-03-17
========================
* [DEVEL] 更新至最新的 testing 分支 (commaai:devel-staging 0.7.4)。
* [DEVEL] 加入動態調整車距功能。(特別感謝 @ShaneSmiskol 提供 PR)

2020-03-15
========================
* [0.7.3] 更新至 2020-03-15 DEVEL。
* [TESTING] "devel" 分支名改為 "testing"。(搶鮮版)

2020-03-14
========================
* [DEVEL] 更新 pt-Br (葡萄牙語) 翻譯。(感謝 berno22 提供)
* [DEVEL] 加入自動關機開關。(感謝 Rzxd 建議)
* [DEVEL] 調高 Toyota 扭力容錯值。
* [DEVEL] 優化讀取 dp 設定值。
* [DEVEL] 加入 2019 手動 Civic 指紋。感謝 (AlexNoop 提供)
* [DEVEL] dp 功能加入對 Subaru 車系的支援。

2020-03-06
========================
* [DEVEL] 加入葡萄牙語支持。(感謝 berno22 提供)
* [DEVEL] 加入大陸 2018 Camry、2020 RAV4 指紋。(感謝 笨木匠 提供)
* [DEVEL] 建立 devel-i18n 取代 devel-en。
* [DEVEL] devel-en is deprecated, please switch to devel-i18n instead.

2020-03-04
========================
* [DEVEL] 加入顯示駕駛監控畫面。
* [DEVEL] 加入加速模式選項。(特別感謝 @arne182, @cgw1968-5779 提供 PR)
* [DEVEL] 修正 shutdownd 在 comma two 可能會不正常關機的錯誤。(感謝 @Wei, @Rzxd 回報)

2020-02-25
========================
* [DEVEL] 更新至最新的 commaai:devel (0.7.3)。
* [0.7.3] 建立，基於 2020-02-25 DEVEL。 

2020-02-21
========================
* [DEVEL] 更新至最新的 commaai:devel (0.7.3)。

2020-02-14
========================
* [DEVEL] 更新至最新的 commaai:devel (0.7.2)。
* [DEVEL] 修正錯誤。
* [0.7.2] 建立，基於 2020-02-14 DEVEL。 

2020-02-08
========================
* [DEVEL] 更新至最新的 commaai:devel (0.7.2)。
* [DEVEL] dp 功能加入對現代 (Hyundai) 車系的支援。
* [DEVEL] 加入神盾測速照相自動啟動的開關。
* [DEVEL] 更新高德地圖至 v4.5.0.600053。
* [DEVEL] 使用 0.6.6 版的更新系統。
* [DEVEL] 修正急剎問題。(感謝 kumar 提供)

2020-02-03
========================
* [0.7.1] 更新至 2020-01-31 DEVEL。

2020-01-31
========================
* [DEVEL] 移除行車介面電量、溫度顯示，(修正畫面當機、黑屏問題)

2020-01-29
========================
* [DEVEL] 修正行車介面錯誤。(感謝 深鲸希西 測試；eisenheim、HeatNation 反應)

2020-01-23
========================
* [DEVEL] 加入 Steer Ratio Learner 關閉。(感謝 eisenheim 建議)
* [DEVEL] 行車介面加入電量、溫度。(感謝 eisenheim 建議)
* [DEVEL] 優化 appd。
* [0.7.1] 建立，基於 2020-01-23 DEVEL。 

2020-01-19
========================
* [DEVEL] 更新至最新的 commaai:devel (0.7.1)。
* [DEVEL] 調整 appd 和 ALC 邏輯。 

2020-01-14
========================
* [DEVEL] 加入開機啟動個人熱點。(感謝 eisenheim 建議)

2020-01-08
========================
* [DEVEL][TOYOTA] 加入大陸版 2018 Lexus RX300 支援。(感謝 cafe 提供)
* [DEVEL] 加入 DragonBTG 設定。(感謝 CloudJ、低調哥、歐姓Altis車主 提供)

2019-12-31
========================
* [DEVEL-ZHS] 加回第三方應用。
* [0.7.0] 建立，基於 2019-12-31 DEVEL。 

2019-12-29
========================
* [DEVEL] 更新至最新的 commaai:devel (0.7.0)。
* [DEVEL] 輔助/自動變道改為可調整參數 (進階用戶)。(DragonAssistedLCMinMPH、DragonAutoLCMinMPH、DragonAutoLCDelay)
* [DEVEL-ZHS] 修正無法運行第三方應用錯誤。(感謝 深鲸希西 反應)

2019-12-18
========================
* [DEVEL] 修正自動換道邏輯。
* [DEVEL] 更新 offroad 翻譯。
* [DEVEL] 錯誤修正。
* [DEVEL] 移除美版 2017 Civic Hatchback 指紋。(與其它車型衝突)

2019-12-17
========================
* [DEVEL] 更新至最新的 commaai:devel (0.7.0)。
* [DEVEL] 加入輔助換道開關。（24mph / 40kph 以上)
* [DEVEL] 加入自動換道開關。（40mph / 65kph 以上)
* [DEVEL] [TOYOTA] 加入大陸版 2019 雷凌汽油版指紋。 (感謝 Shell 提供)
* [DEVEL] [TOYOTA] 加入大陸版 2019 卡羅拉汽油版指紋。 (感謝 Shell 提供)
* [DEVEL] [HONDA] 加入美版 2017 Civic Hatchback 指紋。(感謝 CFranHonda 提供)

2019-12-10
========================
* [DEVEL] 加入位智車機模式。 (Waze Mode)

2019-11-21
========================
* [DEVEL] 修正 offroad 翻譯。(感謝 鄧育林 回報)
* [DEVEL] 調整前車靜止移動偵測參數。
* [DEVEL] 前車靜止移動偵測可在未啟用 dp 時運作。

2019-11-18
========================
* [DEVEL] 修正 offroad 翻譯。(感謝 Cody、鄧育林 回報)

2019-11-18
========================
* [DEVEL] 修正 frame 翻譯。

2019-11-15
========================
* [DEVEL] [0.6.6] 修正不會充電的錯誤。 (感謝 袁昊 反應)

2019-11-15
========================
* [DEVEL] 修正充電控制。 (感謝 KT 反應)
* [DEVEL] 更新 frame 翻譯，改為多語言版。 (感謝 深鲸希西、shaoching885、鄧育林 反應)
* [DEVEL] 更新至最新的 commaai:devel (0.6.6)。
* [0.6.6] 更新至 2019-11-15 DEVEL。

2019-11-12
========================
* [DEVEL] 只顯示電量文字 (注意：有時不會更新，需要拔插 USB 線)
* [DEVEL] 自動偵測並鎖定硬體 (EON / UNO)。

2019-11-12
========================
* [DEVEL] 加入鎖定硬體 (EON / UNO) 的程式碼。
* [0.6.6] 建立，基於 2019-11-12 DEVEL

2019-11-11
========================
* [DEVEL] 更新高德地圖至 v4.3.0.600310 R2098NSLAE
* [DEVEL] 更新 MiXplorer 至 v6.40.3
* [DEVEL] 更新至最新的 commaai:devel (0.6.6)。
* [DEVEL] 前車靜止移動偵測加入偵測警示。

2019-11-07
========================
* [DEVEL] 讓 Bosch 系統顯示三角。 (感謝 ching885 回報)
* [DEVEL] 更新 offroad 多語言版簡體中文翻譯 (感謝 Rming 提供)

2019-11-06
========================
* [DEVEL] 修正 0.6.6 appd 和 dashcamd 錯誤。 (感謝 鄧育林 回報)
* [DEVEL] 更新至最新的 commaai:devel (0.6.6)。
* [0.6.5] 更新至 2019-11-01 DEVEL。

2019-11-05
========================
* [DEVEL] [TOYOTA] 加入台灣 Lexus 2017 GS450h 支援。 (感謝 簡銘佑 提供指紋)

2019-11-01
========================
* [DEVEL] 新增神盾測速照相。 (感謝 Sky Chang 和 Wei Yi Chen)
* [DEVEL] 修正 offroad 翻譯。 (感謝 Leo Hsieh)

2019-11-01
========================
* [DEVEL] 移除 Miui 字型，縮小 dp 使用空間。
* [DEVEL] 更新 offroad 為多語言版
* [DEVEL] 更新至最新的 commaai:devel (0.6.5)。
* [0.6.5] 更新至 2019-10-31 DEVEL。

2019-10-29
========================
* [DEVEL] 加入 SnG 補丁。（感謝 楊雅智)

2019-10-28
========================
* [DEVEL] 更新至最新的 commaai:devel (0.6.5)。
* [DEVEL] 調整 dragon_allow_gas 邏輯 (請回報任何問題，需更新 Panda 韌體)

2019-10-22
========================
* [0.6.5] 移除強迫網路連線提示。(感謝 Shell)

2019-10-18
========================
* [DEVEL] 加入前車靜止移動偵測。(測試版，感謝 ucolchen)
* [DEVEL] 移除強迫網路連線提示。(感謝 Shell)
* [DEVEL] 修正 allow_gas 功能。

2019-10-18
========================
* [DEVEL] 加入彎道減速功能開關。
* [DEVEL] 強迫使用 dp 版 Panda 韌體。
* [DEVEL] 更新至最新的 commaai:devel (0.6.5)。 
* [0.6.5] 更新至 2019-10-18 DEVEL。

2019-10-17
========================
* [DEVEL] 加入「車型」顯示於 dp 設定畫面。
* [DEVEL] 修正充電控制讀取預設值的錯誤。
* [DEVEL] 修正無法顯示更新記錄的錯誤。

2019-10-16
========================
* [DEVEL] 刷新 Panda 韌體按鈕將會自動重啟 EON。(感謝 鄧育林 建議)
* [DEVEL] 下載更新記錄時使用 "no-cache" 標頭。
* [DEVEL] 更新高德地圖至 v4.3.0
* [DEVEL] 刪除 bs (Branch Switcher)

2019-10-15
========================
* [0.6.5] 建立，基於 2019-10-15 DEVEL

2019-10-14
========================
* [DEVEL] 啟用自動更新功能。(感謝 鄧育林 提供)
* [DEVEL] 清除不再使用的 dp params。
* [DEVEL] 加入數字電量指示。(感謝 鄧育林 建議)
* [DEVEL] 加入刷新 Panda 韌體按鈕。

2019-10-11
========================
* [DEVEL] 更新至最新的 commaai:devel (0.6.5)。 
* [DEVEL] [TOYOTA] 加入台灣 2019 RAV4 汽油版指紋。 (感謝 Max Duan / CloudJ 提供)

2019-10-09
========================
* [DEVEL] 加入當 LatCtrl 關閉時，畫面顯示提示訊息。
* [0.6.4] 更新至 2019-10-09
* [0.6.3] 加入台灣版 2019 RAV4H 油電版指紋。

2019-10-08
========================
* [DEVEL] 加回駕駛監控開關。
* [DEVEL] 加入 bs (branch switcher) 程式。

2019-10-07
========================
* [DEVEL] [TOYOTA] 加入台灣版 2019 RAV4H 油電版指紋。(感謝 Max Duan 提供)

2019-10-05
========================
* [DEVEL] 移除 curvature learner: 轉角明顯比原廠小。
* [DEVEL] 更新至最新的 commaai:devel (0.6.4)。 

2019-09-30
========================
* [DEVEL] 更新 curvature learner 版本至 v4。
* [DEVEL] [TOYOTA] Lexus ISH 使用更精確的 EPS Steering Angle Sensor 
* [0.6.4] 更新至 2019-09-30 DEVEL

2019-09-27
========================
* [DEVEL] 加入 Zorrobyte 的 curvature learner (https://github.com/zorrobyte/openpilot)
* [DEVEL] 加入可開關駕駛監控的程式碼。
* [DEVEL] [TOYOTA] 取消當 steering 出現錯誤時，自動切斷方向控制 2 秒的機制。
* [DEVEL] 讓行車介面的「方向盤」/「轉彎」圖示半透明化。

2019-09-26
========================
* [DEVEL] 修正當「啟用記錄服務」關閉時，make 會有問題的錯誤。 (感謝 shaoching885 和 afa 回報)

2019-09-24
========================
* [DEVEL] 行車介面加入可開關的「前車」、「路線」、「車道」設定。
* [DEVEL] 行車介面加入可開關的「方向燈號」提示。 (感謝 CloudJ 建議，程式碼來源: https://github.com/kegman/openpilot)

2019-09-23
========================
* [DEVEL] 優化讀取 params 的次數。
* [DEVEL] [TOYOTA] 加入可開關的車道偏移警示。
* [DEVEL] 修正充電控制邏輯。
* [DEVEL] [TOYOTA] 加入台灣 Prius 4.5 指紋。 (感謝 Lin Hsin Hung 提供)

2019-09-20
========================
* [DEVEL] 加入充電控制功能。 (感謝 loveloveses 和 KT 建議)

2019-09-17
========================
* [0.6.4] 更新包含最新的 DEVEL

2019-09-16
========================
* [DEVEL] [TOYOTA] 加入台灣 CT200h 指紋。 (感謝 CloudJ 提供)
* [DEVEL] [TOYOTA] 加入美版 CT200h 移植。 (感謝 thomaspich 提供)

2019-09-13
========================
* [DEVEL] 行車介面加入可開關的「速度顯示」設定。

2019-09-09
========================
* [DEVEL] 加入 GreyPanda 模式。

2019-08-28
========================
* [DEVEL] 加入可調警示音量。

2019-08-27
========================
* [DEVEL] 自動關機改為可調時長。
