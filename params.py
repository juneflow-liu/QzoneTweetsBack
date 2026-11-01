import requests

cookies = {
    'eas_sid': 'X1D7W7r2R8x0W0b1g8g7h6U442',
    'uin': 'o2926412192',
    'skey': '@SoGODZmkk',
    'RK': 'RfQL/V41uu',
    'ptcz': '6653eaf737100558b08da1bd43e9bac8383361268e1326948c01358f650cc0b5',
    'p_uin': 'o2926412192',
    'pt4_token': 'SrXABtsnnfQJ-khk1ROi4UZYQbjbRjWTNRhL6q3cBYM_',
    'p_skey': 'c7dEqHTjpQNvfmBqTCB5bIJw70huKtMflVTtMrW495c_',
    'Loading': 'Yes',
    'media_p_uin': '2926412192',
    'qz_screen': '1920x1080',
    'pgv_pvid': '6390597313',
    'pgv_info': 'ssid=s6492265900',
    'QZ_FE_WEBP_SUPPORT': '1',
    'media_p_skey': 'BQqjc7s1pZFpotgAB0MTQQK2Vix1qoWdEAHjbLD6yHJgSZHS7Ya2TqqWFRUxnf1P_1JBFMll2r9YWocHEg4CJw',
    '_qimei_uuid42': '1ab0116171a10003829eb59b162ded924ec975e825',
    '_qimei_fingerprint': 'c0b8d5fb051e52451b5c974f35fe4900',
    '_qimei_q36': '',
    '_qimei_h38': '8f95e40e829eb59b162ded920200000961ab01',
    'cpu_performance_v8': '25',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=1, i',
    'referer': 'https://user.qzone.qq.com/2926412192/infocenter',
    'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="141", "Google Chrome";v="141", "SLBrowser";v="9"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 SLBrowser/9.0.8.9131 SLBChan/33 SLBVPV/64-bit',
    # 'cookie': 'eas_sid=X1D7W7r2R8x0W0b1g8g7h6U442; uin=o2926412192; skey=@SoGODZmkk; RK=RfQL/V41uu; ptcz=6653eaf737100558b08da1bd43e9bac8383361268e1326948c01358f650cc0b5; p_uin=o2926412192; pt4_token=SrXABtsnnfQJ-khk1ROi4UZYQbjbRjWTNRhL6q3cBYM_; p_skey=c7dEqHTjpQNvfmBqTCB5bIJw70huKtMflVTtMrW495c_; Loading=Yes; media_p_uin=2926412192; qz_screen=1920x1080; pgv_pvid=6390597313; pgv_info=ssid=s6492265900; QZ_FE_WEBP_SUPPORT=1; media_p_skey=BQqjc7s1pZFpotgAB0MTQQK2Vix1qoWdEAHjbLD6yHJgSZHS7Ya2TqqWFRUxnf1P_1JBFMll2r9YWocHEg4CJw; _qimei_uuid42=1ab0116171a10003829eb59b162ded924ec975e825; _qimei_fingerprint=c0b8d5fb051e52451b5c974f35fe4900; _qimei_q36=; _qimei_h38=8f95e40e829eb59b162ded920200000961ab01; cpu_performance_v8=25',
}

params = {
    'uin': '2926412192',
    'begin_time': '0',
    'end_time': '0',
    'getappnotification': '1',
    'getnotifi': '1',
    'has_get_key': '0',
    'offset': '0',
    'set': '1',
    'count': '10',
    'useutf8': '1',
    'outputhtmlfeed': '1',
    'grz': '0.30314877864246725',
    'scope': '1',
    'g_tk': '933658078',
}

response = requests.get(
    'https://user.qzone.qq.com/proxy/domain/ic2.qzone.qq.com/cgi-bin/feeds/feeds2_html_pav_all',
    params=params,
    cookies=cookies,
    headers=headers,
)
