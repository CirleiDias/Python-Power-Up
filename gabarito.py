# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um textoMOMU000111CEMO000223  Motorola    Celular 3   229.0   55.0        
# FOMO000152  Motorola    Fone    2   150.0   33.0        
# CEMO000271  Motorola    Celular 1   279.0   72.5        
# ACSA0009.3  Samsung Acessorios  3   9.55    2.1     
# ACAP000192  Apple   Acessorios  2   19.0    3.8     
# ACAP000391  Apple   Acessorios  1   39.99   11.9        
# NODE0001614 Dell    Notebook    14  1600.0  352.0       
# NOLE0001713 Lenovo  Notebook    13  1750.0  455.0       
# NORA0007912 Razer   Notebook    12  7999.0  2159.7      
# NORA0001911 Razer   Notebook    11  1999.0  439.8       
# NORA0001110 Razer   Notebook    10  1199.0  299.8       
# NORA000399  Razer   Notebook    9   3999.0  1079.7      
# NOLE000248  Lenovo  Notebook    8   249.0   49.8        
# NOLE000147  Lenovo  Notebook    7   1487.0  386.6       
# NODE000126  Dell    Notebook    6   1220.0  244.0       
# NOHP000165  HP  Notebook    5   1600.0  368.0       
# NOHP000824  HP  Notebook    4   820.0   164.0       
# NOLG000133  LG  Notebook    3   1393.0  334.3       
# NOAS000702  Asus    Notebook    2   700.0   161.0       
# NOAS000691  Asus    Notebook    1   6999.0  1399.8      
# CEMO000197  Motorola    Celular 7   199.0   39.8        
# CEMO000996  Motorola    Celular 6   99.0    28.7        
# CEMO000695  Motorola    Celular 5   69.0    17.3        
# CEMO000114  Motorola    Celular 4   119.0   29.8        
# CEMO000893  Motorola    Celular 3   89.0    26.7        
# CEMO000152  Motorola    Celular 2   150.0   45.0        
# CEMO000101  Motorola    Celular 1   100.0   24.0        
# NOAS0001920 Asus    Notebook    20  1999.0  539.7       
# NOHP0004919 HP  Notebook    19  4999.0  999.8       
# NOVA0003118 Vaio    Notebook    18  319.0   86.1        
# NOPO0003217 Positivo    Notebook    17  320.0   80.0        
# NOPO0003416 Positivo    Notebook    16  349.0   104.7       
# NOCO0003815 Compaq  Notebook    15  380.0   114.0       
# NOAC0007014 Acer    Notebook    14  700.0   154.0       
# NOLE0009913 Lenovo  Notebook    13  999.0   269.7       
# NOMI0003612 Microsoft   Notebook    12  3600.0  972.0       
# NOMI0001911 Microsoft   Notebook    11  1999.0  419.8       
# NOMI0002110 Microsoft   Notebook    10  2199.0  637.7       
# NOMI000999  Microsoft   Notebook    9   999.0   239.8       
# NOLE000298  Lenovo  Notebook    8   299.0   65.8        
# NOSA000547  Samsung Notebook    7   549.0   115.3       
# NOLE000346  Lenovo  Notebook    6   349.0   101.2       
# NOSA000395  Samsung Notebook    5   399.0   103.7       
# NODE000544  Dell    Notebook    4   549.0   137.3       
# NOAC000123  Acer    Notebook    3   1249.0  374.7       
# NODE000502  Dell    Notebook    2   5099.0  1478.7      
# NOAP000501  Apple   Notebook    1   5099.0  1070.8      
# ACSA0001211 Samsung Acessorios  11  12.5    2.8     
# ACSA0001410 Samsung Acessorios  10  14.9    3.2     
# ACSA0008.9  Samsung Acessorios  9   8.9 2.4     
# ACSA000298  Samsung Acessorios  8   29.99   8.9     
# ACSA000247  Samsung Acessorios  7   24.99   8.2     
# ACSA000196  Samsung Acessorios  6   19.99   6.5     
# ACAP000295  Apple   Acessorios  5   29.0    5.8     
# ACAP000194  Apple   Acessorios  4   19.0    3.8     
# ACAP000293  Apple   Acessorios  3   29.0    5.8     
# ACAP000222  Apple   Acessorios  2   22.0    4.4     
# ACAP000191  Apple   Acessorios  1   19.0    3.8     
# CaSO000347  Sony    Camera  7   3498.0  874.5       
# CaSO000996  Sony    Camera  6   998.0   299.4       
# CaSO000165  Sony    Camera  5   1698.0  441.5       
# CaSO000124  Sony    Camera  4   1298.0  298.5       
# CaSO000153  Sony    Camera  3   1598.0  479.4       
# CaSO000212  Sony    Camera  2   2198.0  461.6       
# CaNI000251  Nikon   Camera  1   2596.95 811.1       
# MODE000281  Dell    Mouse   1   28.99   8.7     
# MOSA000171  Samsung Monitor 1   179.99  46.8        
# TEMU0008.1  Multilaser  Teclado 1   8.99    1.8     
# MODE000141  Dell    Mouse   1   14.99   4.6     
# MOSA000121  Samsung Monitor 1   129.99  45.5        
# TEMU000211  Multilaser  Teclado 1   21.99   4.4     
# MODE000191  Dell    Mouse   1   19.99   5.8     
# CaNI000214  Nikon   Camera  4   2196.95 527.3       
# CaNI000793  Nikon   Camera  3   796.95  239.1       
# CaNI000272  Nikon   Camera  2   2796.95 643.3       
# CaNI000131  Nikon   Camera  1   1396.0  349.0       
# MOSA000191  Samsung Monitor 1   199.99  52.0        
# TELG000101  LG  Teclado 1   10.0    2.5     
# MOLO000151  Logitech    Mouse   1   15.99   5.1     
# CaCA000894  Canon   Camera  4   899.0   260.7       
# CaCA000483  Canon   Camera  3   489.0   107.6       
# CaCA000502  Canon   Camera  2   509.0   112.0       
# CaCA000581  Canon   Camera  1   589.0   176.7       
# RESA0002410 Samsung Relogio 10  240.0   55.2        
# REGA000809  Garmin  Relogio 9   800.0   160.0       
# REGA000928  Garmin  Relogio 8   920.0   239.2       
# REAP000327  Apple   Relogio 7   320.0   92.8        
# REAP000446  Apple   Relogio 6   440.0   118.8       
# REAP000485  Apple   Relogio 5   480.0   120.0       
# REAP000504  Apple   Relogio 4   500.0   110.0       
# REAP000643  Apple   Relogio 3   640.0   179.2       
# REAP000702  Apple   Relogio 2   700.0   182.0       
# REAP000101  Apple   Relogio 1   1080.0  280.8       
# TESO0005913 Sony    Televisao   13  599.0   131.8       
# TESO0006012 Sony    Televisao   12  600.0   138.0       
# TESO0003311 Sony    Televisao   11  3300.0  726.0       
# TESO0001210 Sony    Televisao   10  1200.0  240.0       
# TELG000559  LG  Televisao   9   550.0   148.5       
# TELG000398  LG  Televisao   8   390.0   93.6        
# TEIN000187  Insignia    Televisao   7   189.99  45.6        
# TEIN000346  Insignia    Televisao   6   343.0   82.3        
# TEIN000255  Insignia    Televisao   5   250.0   65.0        
# TEVI000244  Vizio   Televisao   4   240.0   69.6        
# TEVI000443  Vizio   Televisao   3   440.0   110.0       
# TEVI000152  Vizio   Televisao   2   159.0   36.6        
# TETC000121  TCL Televisao   1   1200.0  240.0       
# NOAP000599  Apple   Notebook    9   5999.0  1679.7      
# NOAP000128  Apple   Notebook    8   1299.0  337.7       
# NOAP000247  Apple   Notebook    7   2499.0  599.8       
# NOAP000646  Apple   Notebook    6   6400.0  1280.0      
# NOAP000255  Apple   Notebook    5   2549.0  688.2       
# NOAP000144  Apple   Notebook    4   1499.0  419.7       
# NOHP000943  HP  Notebook    3   949.0   237.3       
# NOAC000791  Acer    Notebook    1   799.0   159.8       
# NOMU000192    Multilaser  Notebook    2   199.0   41.8        
# CAHA000124  Hashtag Casaco  4   12.9    6.1     
# CAHA000123  Hashtag Casaco  3   12.9    6.1     
# BEHA000482  Hashtag Bermuda 2   48.9    20.0        
# MOLG000782  LG  Monitor 2   789.99  221.2       
# BEHA000481    Hashtag Bermuda 1   48.9    20.0        
# TELG000201  LG  Teclado 1   20.0    4.6     
# MOSP0007.3  Spectre Mouse   3   7.99    2.0     
# MOSP000132  Spectre Monitor 2   132.72  38.5        
# MOSP000221  Spectre Monitor 1   229.99  59.8        
# CAHA000482  Hashtag Casaco  2   48.9    20.0        
# CAHA000481  Hashtag Casaco  1   48.9    20.0        
# TELG000111  LG  Teclado 1   110.0   29.7        
# MOLO0006.3  Logitech    Mouse   3   6.99    2.3     
# MOMU0003.2  Multilaser  Mouse   2   3.99    1.3     
# MOMU0004.1  Multilaser  Mouse   1   4.99    1.2     
# CAHA0004521 Hashtag Casaco  21  45.9    19.7        
# CAHA0004520 Hashtag Casaco  20  45.9    19.7        
# CAHA0004519 Hashtag Casaco  19  45.9    19.7        
# CAHA0004518 Hashtag Casaco  18  45.9    19.7        
# CAHA0004817 Hashtag Casaco  17  48.9    20.0        
# CAHA0004816 Hashtag Casaco  16  48.9    20.0        
# CAHA0004815 Hashtag Casaco  15  48.9    20.0        
# CAHA0004814 Hashtag Casaco  14  48.9    20.0        
# CAHA0004513 Hashtag Casaco  13  45.9    19.7        
# CAHA0004512 Hashtag Casaco  12  45.9    19.7        
# CAHA0004511 Hashtag Casaco  11  45.9    19.7        
# CAHA0004510 Hashtag Casaco  10  45.9    19.7        
# CAHA0009.9  Hashtag Camisa  9   9.9 4.5     
# CAHA000278  Hashtag Camisa  8   27.0    12.4        
# CAHA000277  Hashtag Camisa  7   27.0    12.4        
# CAHA000276  Hashtag Camisa  6   27.0    12.4        
# CHHA000275  Hashtag Chaveiro    5   27.0    12.4        
# CAHA000254  Hashtag Camisa  4   25.0    11.0        
# CAHA000253  Hashtag Camisa  3   25.0    11.0        
# MOHA000252  Hashtag Mochila 2   25.0    11.0        
# MOHA000251  Hashtag Mochila 1   25.0    11.0        
# MOLG000173  LG  Monitor 3   1796.99 467.2       
# MOSA000152  Samsung Monitor 2   159.99  41.6        
# MOLG000121  LG  Monitor 1   129.0   34.8        
# TEDE000484  Dell    Teclado 4   48.0    11.5        
# TELO000443  Logitech    Teclado 3   44.0    11.0        
# TEDE000362  Dell    Teclado 2   36.0    8.3     
# TELO000131  Logitech    Teclado 1   138.0   37.3        
# CAHA000271  Hashtag Camisa  1   27.5    12.4        
# NOLE0009911 Lenovo  Notebook    11  999.0   259.7       
# NOHP0007510 HP  Notebook    10  750.0   210.0       
# NODE000749  Dell    Notebook    9   740.0   170.2       
# NODE000608  Dell    Notebook    8   600.0   132.0       
# NOAC000127  Acer    Notebook    7   1299.0  285.8       
# NOAC000216  Acer    Notebook    6   2199.0  483.8       
# NOAC000525  Acer    Notebook    5   529.99  143.1       
# NOHP000594  HP  Notebook    4   599.0   131.8       
# NOAS000153  Asus    Notebook    3   1599.0  415.7       
# NODE000492  Dell    Notebook    2   498.0   109.6       
# NOLE000741  Lenovo  Notebook    1   749.0   224.7       
# CEMO0009925 Motorola    Celular 25  99.0    25.7        
# CEMO0006924 Motorola    Celular 24  69.0    18.6        
# CEXI0003523 Xiaomi  Celular 23  350.0   122.27      
# CEXI0002722 Xiaomi  Celular 22  279.0   49.98       
# CEXI0002521 Xiaomi  Celular 21  250.0   145.28      
# CEXI0002420 Xiaomi  Celular 20  249.0   104.8       
# CEXI0002919 Xiaomi  Celular 19  299.0   38.96       
# CEXI0003218 Xiaomi  Celular 18  329.0   75.7        
# CEXI0002417 Xiaomi  Celular 17  249.0   96.8        
# CEXI0002116 Xiaomi  Celular 16  219.0   56.9        
# CEXI0001515 Xiaomi  Celular 15  159.0   42.9        
# CEXI0003114 Xiaomi  Celular 14  317.0   133.3       
# CEXI0002513 Xiaomi  Celular 13  257.0   74.5        
# CESA0002012 Samsung Celular 12  200.0   92.81       
# CESA0001511 Samsung Celular 11  150.0   26.97       
# CESA0001210 Samsung Celular 10  120.0   31.2        
# CESA000909  Samsung Celular 9   900.0   198.0       
# CESA000808  Samsung Celular 8   800.0   176.0       
# CESA000107  Samsung Celular 7   100.0   27.0        
# CESA000276  Samsung Celular 6   270.0   81.0        
# CESA000205  Samsung Celular 5   200.0   56.0        
# CESA000154  Samsung Celular 4   150.0   31.5        
# CESA000103  Samsung Celular 3   100.0   28.0        
# CESA000402  Samsung Celular 2   400.0   96.0        
# CESA000301  Samsung Celular 1   300.0   66.0        
# REAP000783  Apple   Relogio 3   789.0   228.8       
# RESA000602  Samsung Relogio 2   60.0    15.6        
# RESA000501  Samsung Relogio 1   50.0    14.5        
# NOAS0006213 Asus    Notebook    13  629.99  189.0       
# NOHP0003512 HP  Notebook    12  359.0   100.5       
# NOSA0001311 Samsung Notebook    11  1349.99 270.0       
# NOHP0005210 HP  Notebook    10  529.0   111.1       
# NOLE000989  Lenovo  Notebook    9   989.99  217.8       
# NOHP000238  HP  Notebook    8   239.88  64.8        
# NOHP000797  HP  Notebook    7   799.0   199.8       
# NOMI000426  Microsoft   Notebook    6   429.0   90.1        
# NOHP000215  HP  Notebook    5   214.0   49.2        
# NOAC000224  Acer    Notebook    4   227.0   65.8        
# NOLE000183  Lenovo  Notebook    3   188.61  41.5        
# NODE000512  Dell    Notebook    2   512.0   107.5       
# NODE000441  Dell    Notebook    1   448.0   134.4       
# CESA0002040 Samsung Celular 40  200.0   48.0        
# CEAP0005439 Apple   Celular 39  549.0   142.7       
# CEAP0004938 Apple   Celular 38  499.0   124.8       
# CEAP0004937 Apple   Celular 37  499.0   129.7       
# CEAP0004436 Apple   Celular 36  449.0   103.3       
# CEAP0006435 Apple   Celular 35  649.0   142.8       
# CEAP0005434 Apple   Celular 34  549.0   120.8       
# CEAP0006933 Apple   Celular 33  699.0   181.7       
# CEAP0005932 Apple   Celular 32  599.0   137.8       
# CEAP0008431 Apple   Celular 31  849.0   178.3       
# CEAP0006430 Apple   Celular 30  649.0   181.7       
# CEAP0005429 Apple   Celular 29  549.0   115.3       
# CEAP0009428 Apple   Celular 28  949.0   256.2       
# CEAP0007427 Apple   Celular 27  749.0   157.3       
# CEAP0006426 Apple   Celular 26  649.0   181.7       
# CEAP0001325 Apple   Celular 25  1349.0  296.8       
# CEAP0001124 Apple   Celular 24  1149.0  252.8       
# CEAP0009423 Apple   Celular 23  949.0   256.2       
# CEAP0008422 Apple   Celular 22  849.0   178.3       
# CEAP0001421 Apple   Celular 21  1449.0  347.8       
# CEAP0001220 Apple   Celular 20  1249.0  362.2       
# CEAP0001019 Apple   Celular 19  1049.0  304.2       
# CEAP0009418 Apple   Celular 18  949.0   256.2       
# CEAP0005717 Apple   Celular 17  579.0   115.8       
# CEAP0004716 Apple   Celular 16  479.0   138.9       
# CEAP0004215 Apple   Celular 15  429.0   115.8       
# CEAP0009914 Apple   Celular 14  999.0   269.7       
# CEAP0007913 Apple   Celular 13  799.0   215.7       
# CEAP0006912 Apple   Celular 12  699.0   167.8       
# CEAP0001011 Apple   Celular 11  1099.0  329.7       
# CEAP0008910 Apple   Celular 10  899.0   197.8       
# CEAP000799  Apple   Celular 9   799.0   215.7       
# CEAP000148  Apple   Celular 8   1499.0  329.8       
# CEAP000127  Apple   Celular 7   1299.0  298.8       
# CEAP000106  Apple   Celular 6   1099.0  329.7       
# CEAP000995  Apple   Celular 5   999.0   269.7       
# CEAP000154  Apple   Celular 4   1599.0  367.8       
# CEAP000133  Apple   Celular 3   1399.0  377.7       
# CEAP000112  Apple   Celular 2   1199.0  287.8       
# CEAP000101  Apple   Celular 1   1099.0  329.7       
# RESA0003210 Samsung Relogio 10  320.0   83.2        
# RESA000389  Samsung Relogio 9   380.0   110.2       
# RESA000298  Samsung Relogio 8   290.0   72.5        
# RESA000287  Samsung Relogio 7   280.0   72.8        
# REXI000116  Xiaomi  Relogio 6   114.0   23.9        
# REXI000365  Xiaomi  Relogio 5   36.0    7.9     
# REXI000744  Xiaomi  Relogio 4   74.0    15.5        
# REXI000463  Xiaomi  Relogio 3   46.4    11.6        
# REGA000722  Garmin  Relogio 2   720.0   187.2       
# REGA000441  Garmin  Relogio 1   440.0   96.8        
# TETC0002222 TCL Televisao   22  220.0   59.4        
# TETC0001521 TCL Televisao   21  158.0   36.3        
# TEPH0002720 Philco  Televisao   20  279.8   56.0        
# TEPH0004019 Philco  Televisao   19  400.0   120.0       
# TESE0005018 SEMP    Televisao   18  500.0   140.0       
# TESE0003817 SEMP    Televisao   17  380.0   91.2        
# TESE0005016 SEMP    Televisao   16  500.0   125.0       
# TETO0006015 Toshiba Televisao   15  600.0   144.0       
# TETO0008014 Toshiba Televisao   14  800.0   192.0       
# TETO0006413 Toshiba Televisao   13  640.0   185.6       
# TEAO0003612 AOC Televisao   12  360.0   97.2        
# TEAO0002511 AOC Televisao   11  250.0   62.5        
# TESA0002010 Samsung Televisao   10  2000.0  440.0       
# TESA000729  Samsung Televisao   9   720.0   201.6       
# TESA000108  Samsung Televisao   8   10000.0 3000.0      
# TESA000747  Samsung Televisao   7   740.0   214.6       
# TESA000346  Samsung Televisao   6   340.0   71.4        
# TESA000125  Samsung Televisao   5   1260.0  378.0       
# TELG000524  LG  Televisao   4   520.0   145.6       
# TELG000373  LG  Televisao   3   378.0   83.2        
# TELG000252  LG  Televisao   2   250.0   62.5        
# TELG000821  LG  Televisao   1   820.0   172.2       
# CAHA000275  Hashtag Camisa  5   27.5    12.4        
# CAHA000274  Hashtag Camisa  4   27.5    12.4        
# CAHA000273  Hashtag Camisa  3   27.5    12.4    Troca de fornecedor 
# BOHA000252  Hashtag Bone    2   25.0    11.0        
# BOHA000251  Hashtag Bone    1   25.0    11.0        
# MOMU000111  Multilaser  Mouse   1   11.99   3.4     
# CAHA000252  Hashtag Camisa  2   25.0    11.0    Conferir estoque    
# CEMO000223  Motorola    Celular 3   229.0   55.0        
# FOMO000152  Motorola    Fone    2   150.0   33.0        
# CEMO000271  Motorola    Celular 1   279.0   72.5        
# ACSA0009.3  Samsung Acessorios  3   9.55    2.1     
# ACAP000192  Apple   Acessorios  2   19.0    3.8     
# ACAP000391  Apple   Acessorios  1   39.99   11.9        
# NODE0001614 Dell    Notebook    14  1600.0  352.0       
# NOLE0001713 Lenovo  Notebook    13  1750.0  455.0       
# NORA0001911 Razer   Notebook    11  1999.0  439.8       
# NORA0007912   Razer   Notebook    12  7999.0  2159.7      
# NORA0001110 Razer   Notebook    10  1199.0  299.8       
# NORA000399  Razer   Notebook    9   3999.0  1079.7      
# NOLE000248  Lenovo  Notebook    8   249.0   49.8        
# NOLE000147  Lenovo  Notebook    7   1487.0  386.6       
# NODE000126  Dell    Notebook    6   1220.0  244.0       
# NOHP000165  HP  Notebook    5   1600.0  368.0       
# NOHP000824  HP  Notebook    4   820.0   164.0       
# NOLG000133  LG  Notebook    3   1393.0  334.3       
# NOAS000702  Asus    Notebook    2   700.0   161.0       
# NOAS000691  Asus    Notebook    1   6999.0  1399.8      
# CEMO000197  Motorola    Celular 7   199.0   39.8        
# CEMO000996  Motorola    Celular 6   99.0    28.7        
# CEMO000695  Motorola    Celular 5   69.0    17.3        
# CEMO000114  Motorola    Celular 4   119.0   29.8        
# CEMO000893  Motorola    Celular 3   89.0    26.7        
# CEMO000152  Motorola    Celular 2   150.0   45.0        
# CEMO000101  Motorola    Celular 1   100.0   24.0        
# NOAS0001920 Asus    Notebook    20  1999.0  539.7       
# NOHP0004919 HP  Notebook    19  4999.0  999.8       
# NOVA0003118 Vaio    Notebook    18  319.0   86.1        
# NOPO0003217 Positivo    Notebook    17  320.0   80.0        
# NOPO0003416 Positivo    Notebook    16  349.0   104.7       
# NOCO0003815 Compaq  Notebook    15  380.0   114.0       
# NOAC0007014 Acer    Notebook    14  700.0   154.0       
# NOLE0009913 Lenovo  Notebook    13  999.0   269.7       
# NOMI0003612 Microsoft   Notebook    12  3600.0  972.0       
# NOMI0001911 Microsoft   Notebook    11  1999.0  419.8       
# NOMI0002110 Microsoft   Notebook    10  2199.0  637.7       
# NOMI000999  Microsoft   Notebook    9   999.0   239.8       
# NOLE000298  Lenovo  Notebook    8   299.0   65.8        
# NOSA000547  Samsung Notebook    7   549.0   115.3       
# NOLE000346  Lenovo  Notebook    6   349.0   101.2       
# NOSA000395  Samsung Notebook    5   399.0   103.7       
# NODE000544  Dell    Notebook    4   549.0   137.3       
# NOAC000123  Acer    Notebook    3   1249.0  374.7       
# NODE000502  Dell    Notebook    2   5099.0  1478.7      
# NOAP000501  Apple   Notebook    1   5099.0  1070.8      
# ACSA0001211 Samsung Acessorios  11  12.5    2.8     
# ACSA0001410 Samsung Acessorios  10  14.9    3.2     
# ACSA0008.9  Samsung Acessorios  9   8.9 2.4     
# ACSA000298  Samsung Acessorios  8   29.99   8.9     
# ACSA000247  Samsung Acessorios  7   24.99   8.2     
# ACSA000196  Samsung Acessorios  6   19.99   6.5     
# ACAP000295  Apple   Acessorios  5   29.0    5.8     
# ACAP000194  Apple   Acessorios  4   19.0    3.8     
# ACAP000293  Apple   Acessorios  3   29.0    5.8     
# ACAP000222  Apple   Acessorios  2   22.0    4.4     
# ACAP000191  Apple   Acessorios  1   19.0    3.8     
# CaSO000347  Sony    Camera  7   3498.0  874.5       
# CaSO000996  Sony    Camera  6   998.0   299.4       
# CaSO000165  Sony    Camera  5   1698.0  441.5       
# CaSO000124  Sony    Camera  4   1298.0  298.5       
# CaSO000153  Sony    Camera  3   1598.0  479.4       
# CaSO000212  Sony    Camera  2   2198.0  461.6       
# CaNI000251  Nikon   Camera  1   2596.95 811.1       
# MODE000281  Dell    Mouse   1   28.99   8.7     
# MOSA000171  Samsung Monitor 1   179.99  46.8        
# TEMU0008.1  Multilaser  Teclado 1   8.99    1.8     
# MODE000141  Dell    Mouse   1   14.99   4.6     
# MOSA000121  Samsung Monitor 1   129.99  45.5        
# TEMU000211  Multilaser  Teclado 1   21.99   4.4     
# MODE000191  Dell    Mouse   1   19.99   5.8     
# CaNI000214  Nikon   Camera  4   2196.95 527.3       
# CaNI000793  Nikon   Camera  3   796.95  239.1       
# CaNI000272  Nikon   Camera  2   2796.95 643.3       
# CaNI000131  Nikon   Camera  1   1396.0  349.0       
# MOSA000191  Samsung Monitor 1   199.99  52.0        
# TELG000101  LG  Teclado 1   10.0    2.5     
# MOLO000151  Logitech    Mouse   1   15.99   5.1     
# CaCA000894  Canon   Camera  4   899.0   260.7       
# CaCA000483  Canon   Camera  3   489.0   107.6       
# CaCA000502  Canon   Camera  2   509.0   112.0       
# CaCA000581  Canon   Camera  1   589.0   176.7       
# RESA0002410 Samsung Relogio 10  240.0   55.2  CAHA000251  Hashtag Camisa  1   25.0    11.0        
#       
# REGA000809  Garmin  Relogio 9   800.0   160.0       
# REGA000928  Garmin  Relogio 8   920.0   239.2       
# REAP000327  Apple   Relogio 7   320.0   92.8        
# REAP000446  Apple   Relogio 6   440.0   118.8       
# REAP000485  Apple   Relogio 5   480.0   120.0       
# REAP000504  Apple   Relogio 4   500.0   110.0       
# REAP000643  Apple   Relogio 3   640.0   179.2       
# REAP000702  Apple   Relogio 2   700.0   182.0       
# REAP000101  Apple   Relogio 1   1080.0  280.8       
# TESO0005913 Sony    Televisao   13  599.0   131.8       
# TESO0006012 Sony    Televisao   12  600.0   138.0       
# TESO0003311 Sony    Televisao   11  3300.0  726.0       
# TESO0001210 Sony    Televisao   10  1200.0  240.0       
# TELG000559  LG  Televisao   9   550.0   148.5       
# TELG000398  LG  Televisao   8   390.0   93.6        
# TEIN000187  Insignia    Televisao   7   189.99  45.6        
# TEIN000346  Insignia    Televisao   6   343.0   82.3        
# TEIN000255  Insignia    Televisao   5   250.0   65.0        
# TEVI000244  Vizio   Televisao   4   240.0   69.6        
# TEVI000443  Vizio   Televisao   3   440.0   110.0       
# TEVI000152  Vizio   Televisao   2   159.0   36.6        
# TETC000121  TCL Televisao   1   1200.0  240.0       
# NOAP000599  Apple   Notebook    9   5999.0  1679.7      
# NOAP000128  Apple   Notebook    8   1299.0  337.7       
# NOAP000247  Apple   Notebook    7   2499.0  599.8       
# NOAP000646  Apple   Notebook    6   6400.0  1280.0      
# NOAP000255  Apple   Notebook    5   2549.0  688.2       
# NOAP000144  Apple   Notebook    4   1499.0  419.7       
# NOHP000943  HP  Notebook    3   949.0   237.3       
# NOMU000192  Multilaser  Notebook    2   199.0   41.8        
# NOAC000791  Acer    Notebook    1   799.0   159.8       
# CAHA000124  Hashtag Casaco  4   12.9    6.1     
# CAHA000123  Hashtag Casaco  3   12.9    6.1     
# BEHA000482  Hashtag Bermuda 2   48.9    20.0        
# BEHA000481  Hashtag Bermuda 1   48.9    20.0        
# MOLG000782  LG  Monitor 2   789.99  221.2       
# TELG000201  LG  Teclado 1   20.0    4.6     
# MOSP0007.3  Spectre Mouse   3   7.99    2.0     
# MOSP000132  Spectre Monitor 2   132.72  38.5        
# MOSP000221  Spectre Monitor 1   229.99  59.8        
# CAHA000482  Hashtag Casaco  2   48.9    20.0        
# TELG000111  LG  Teclado 1   110.0   29.7        
# CAHA000481    Hashtag Casaco  1   48.9    20.0        
#MOLO0006.3  Logitech    Mouse   3   6.99    2.3     
# MOMU0003.2  Multilaser  Mouse   2   3.99    1.3     
# MOMU0004.1  Multilaser  Mouse   1   4.99    1.2     
# CAHA0004521 Hashtag Casaco  21  45.9    19.7        
# CAHA0004520 Hashtag Casaco  20  45.9    19.7        
# CAHA0004519 Hashtag Casaco  19  45.9    19.7        
# CAHA0004518 Hashtag Casaco  18  45.9    19.7        
# CAHA0004817 Hashtag Casaco  17  48.9    20.0        
# CAHA0004816 Hashtag Casaco  16  48.9    20.0        
# CAHA0004815 Hashtag Casaco  15  48.9    20.0        
# CAHA0004814 Hashtag Casaco  14  48.9    20.0        
# CAHA0004513 Hashtag Casaco  13  45.9    19.7        
# CAHA0004511 Hashtag Casaco  11  45.9    19.7        
# CAHA0004510 Hashtag Casaco  10  45.9    19.7  CAHA0004512 Hashtag Casaco  12  45.9    19.7        
#       
# CAHA0009.9  Hashtag Camisa  9   9.9 4.5     
# CAHA000278  Hashtag Camisa  8   27.0    12.4        
# CAHA000277  Hashtag Camisa  7   27.0    12.4        
# CAHA000276  Hashtag Camisa  6   27.0    12.4        
# CHHA000275  Hashtag Chaveiro    5   27.0    12.4        
# CAHA000254  Hashtag Camisa  4   25.0    11.0        
# CAHA000253  Hashtag Camisa  3   25.0    11.0        
# MOHA000252  Hashtag Mochila 2   25.0    11.0        
# MOHA000251  Hashtag Mochila 1   25.0    11.0        
# MOLG000173  LG  MOSA000152  Samsung Monitor 2   159.99  41.6        
# MOLG000121  LG  Monitor 1   129.0   34.8        
# TEDE000484  Dell    Teclado 4   48.0    11.5        
# TELO000443  Logitech    Teclado 3   44.0    11.0        
# TEDE000362  Dell    Teclado 2   36.0    8.3     
# TELO000131  Logitech    Teclado 1   138.0   37.3        
# CAHA000271  Hashtag Camisa  1   27.5    12.4        
# NOLE0009911 Lenovo  Notebook    11  999.0   259.7       
# NOHP0007510 HP  Notebook    10  750.0   210.0       
# NODE000749  Dell    Notebook    9   740.0   170.2       
# NODE000608  Dell    Notebook    8   600.0   132.0       
# NOAC000127  Acer    Notebook    7   1299.0  285.8       
# NOAC000216  Acer    Notebook    6   2199.0  483.8       
# NOAC000525  Acer    Notebook    5   529.99  143.1       
# NOHP000594  HP  Notebook    4   599.0   131.8       
# NOAS000153  Asus    Notebook    3   1599.0  415.7       
# NODE000492  Dell    Notebook    2   498.0   109.6       
# NOLE000741  Lenovo  Notebook    1   749.0   224.7       
# CEMO0009925 Motorola    Celular 25  99.0    25.7        
# CEMO0006924 Motorola    Celular 24  69.0    18.6        
# CEXI0003523 Xiaomi  Celular 23  350.0   122.27      
# CEXI0002722 Xiaomi  Celular 22  279.0   49.98       
# CEXI0002521 Xiaomi  Celular 21  250.0   145.28      
# CEXI0002420 Xiaomi  Celular 20  249.0   104.8       
# CEXI0002919 Xiaomi  Celular 19  299.0   38.96       
# CEXI0003218 Xiaomi  Celular 18  329.0   75.7        
# CEXI0002417 Xiaomi  Celular 17  249.0   96.8        
# CEXI0002116 Xiaomi  Celular 16  219.0   56.9        
# CEXI0001515 Xiaomi  Celular 15  159.0   42.9        
# CEXI0003114 Xiaomi  Celular 14  317.0   133.3       
# CEXI0002513 Xiaomi  Celular 13  257.0   74.5        
# CESA0002012 Samsung Celular 12  200.0   92.81       
# CESA0001511 Samsung Celular 11  150.0   26.97       
# CESA0001210 Samsung Celular 10  120.0   31.2        
# CESA000909  Samsung Celular 9   900.0   198.0       
# CESA000808  Samsung Celular 8   800.0   176.0       
# CESA000107  Samsung Celular 7   100.0   27.0        
# CESA000276  Samsung Celular 6   270.0   81.0        
# CESA000205  Samsung Celular 5   200.0   56.0        
# CESA000154  Samsung Celular 4   150.0   31.5        
# CESA000103  Samsung Celular 3   100.0   28.0        
# CESA000402  Samsung Celular 2   400.0   96.0        
# CESA000301  Samsung Celular 1   300.0   66.0  MOLO000192  Logitech    Mouse   2   19.95   5.0     
#       
# REAP000783  Apple   Relogio 3   789.0   228.8       
# RESA000602  Samsung Relogio 2   60.0    15.6        
# RESA000501  Samsung Relogio 1   50.0    14.5        
# NOAS0006213 Asus    Notebook    13  629.99  189.0       
# NOHP0003512 HP  Notebook    12  359.0   100.5       
# NOSA0001311 Samsung Notebook    11  1349.99 270.0       
# NOHP0005210 HP  Notebook    10  529.0   111.1       
# NOLE000989  Lenovo  Notebook    9   989.99  217.8       
# NOHP000238  HP  Notebook    8   239.88  64.8        
# NOHP000797  HP  Notebook    7   799.0   199.8       
# NOMI000426  Microsoft   Notebook    6   429.0   90.1        
# NOHP000215  HP  Notebook    5   214.0   49.2        
# NOAC000224  Acer    Notebook    4   227.0   65.8        
# NOLE000183  Lenovo  Notebook    3   188.61  41.5        
# NODE000512  Dell    Notebook    2   512.0   107.5       
# NODE000441  Dell    Notebook    1   448.0   134.4       
# CESA0002040 Samsung Celular 40  200.0   48.0        
# CEAP0005439 Apple   Celular 39  549.0   142.7       
# CEAP0004938 Apple   Celular 38  499.0   124.8       
# CEAP0004937 Apple   Celular 37  499.0   129.7       
# CEAP0004436 Apple   Celular 36  449.0   103.3       
# CEAP0006435 Apple   Celular 35  649.0   142.8       
# CEAP0005434 Apple   Celular 34  549.0   120.8       
# CEAP0006933 Apple   Celular 33  699.0   181.7       
# CEAP0005932 Apple   Celular 32  599.0   137.8       
# CEAP0008431 Apple   Celular 31  849.0   178.3       
# CEAP0006430 Apple   Celular 30  649.0   181.7       
# CEAP0005429 Apple   Celular 29  549.0   115.3       
# CEAP0009428 Apple   Celular 28  949.0   256.2       
# CEAP0007427 Apple   Celular 27  749.0   157.3       
# CEAP0006426 Apple   Celular 26  649.0   181.7       
# CEAP0001325 Apple   Celular 25  1349.0  296.8       
# CEAP0001124 Apple   Celular 24  1149.0  252.8       
# CEAP0009423 Apple   Celular 23  949.0   256.2       
# CEAP0008422 Apple   Celular 22  849.0   178.3       
# CEAP0001421 Apple   Celular 21  1449.0  347.8       
# CEAP0001220 Apple   Celular 20  1249.0  362.2       
# CEAP0001019 Apple   Celular 19  1049.0  304.2       
# CEAP0009418 Apple   Celular 18  949.0   256.2       
# CEAP0005717 Apple   Celular 17  579.0   115.8       
# CEAP0004716 Apple   Celular 16  479.0   138.9       
# CEAP0004215 Apple   Celular 15  429.0   115.8       
# CEAP0009914 Apple   Celular 14  999.0   269.7       
# CEAP0007913 Apple   Celular 13  799.0   215.7       
# CEAP0006912 Apple   Celular 12  699.0   167.8       
# CEAP0001011 Apple   Celular 11  1099.0  329.7       
# CEAP0008910 Apple   Celular 10  899.0   197.8       
# CEAP000799  Apple   Celular 9   799.0   215.7       
# CEAP000148  Apple   Celular 8   1499.0  329.8       
# CEAP000127  Apple   Celular 7   1299.0  298.8       
# CEAP000106  Apple   Celular 6   1099.0  329.7       
# CEAP000995  Apple   Celular 5   999.0   269.7       
# CEAP000154  Apple   Celular 4   1599.0  367.8       
# CEAP000133  Apple   Celular 3   1399.0  377.7       
# CEAP000112  Apple   Celular 2   1199.0  287.8       
# CEAP000101  Apple   Celular 1   1099.0  329.7       
# RESA0003210 Samsung Relogio 10  320.0   83.2        
# RESA000389  Samsung Relogio 9   380.0   110.2       
# RESA000298  Samsung Relogio 8   290.0   72.5        
# RESA000287  Samsung Relogio 7   280.0   72.8        
# REXI000116  Xiaomi  Relogio 6   114.0   23.9        
# REXI000365  Xiaomi  Relogio 5   36.0    7.9     
# REXI000744  Xiaomi  Relogio 4   74.0    15.5        
# REXI000463  Xiaomi  Relogio 3   46.4    11.6        
# REGA000722  Garmin  Relogio 2   720.0   187.2       
# REGA000441  Garmin  Relogio 1   440.0   96.8        
# TETC0002222 TCL Televisao   22  220.0   59.4        
# TETC0001521 TCL Televisao   21  158.0   36.3        
# TEPH0002720 Philco  Televisao   20  279.8   56.0        
# TEPH0004019 Philco  Televisao   19  400.0   120.0       
# TESE0005018 SEMP    Televisao   18  500.0   140.0       
# TESE0003817 SEMP    Televisao   17  380.0   91.2        
# TESE0005016 SEMP    Televisao   16  500.0   125.0       
# TETO0006015 Toshiba Televisao   15  600.0   144.0       
# TETO0008014 Toshiba Televisao   14  800.0   192.0       
# TETO0006413 Toshiba Televisao   13  640.0   185.6       
# TEAO0003612 AOC Televisao   12  360.0   97.2        
# TEAO0002511 AOC Televisao   11  250.0   62.5        
# TESA0002010 Samsung Televisao   10  2000.0  440.0       
# TESA000729  Samsung Televisao   9   720.0   201.6       
# TESA000108  Samsung Televisao   8   10000.0 3000.0      
# TESA000747  Samsung Televisao   7   740.0   214.6       
# TESA000346  Samsung Televisao   6   340.0   71.4        
# TESA000125  Samsung Televisao   5   1260.0  378.0       
# TELG000524  LG  Televisao   4   520.0   145.6       
# TELG000373  LG  Televisao   3   378.0   83.2        
# TELG000252  LG  Televisao   2   250.0   62.5        
# TELG000821  LG  Televisao   1   820.0   172.2       
#     Multilaser  Mouse   1   11.99
# pyautogui.press -> apertar 1 teclaBOHA000251  Hashtag Bone    1   25.0

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de CAHA000252  Hashtag Camisa  2   25.0    11.0    Conferir estoque    
pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")    

#chrome
("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# entrar no link 
pyautogui.write("https://dlp.MOLO000251 Logitech    Mouse   1   25.95   6.5.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
#pythonimpressionador@gmail.com  sua senha

# Passo 2: Fazer loginMOLO000251    Logitech    Mouse   1   25.95   6.5     

# selecionar o campo de email
pyautogui.click(x=685, y=451)
# escrever o seu emailpythonimpressionador@gmail.com    sua senha
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=955, y=638) # clique no botao de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
  

