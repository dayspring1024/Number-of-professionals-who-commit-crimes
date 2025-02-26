import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()

plt.rc('font', family=font_name)


doctor = ((588+102)/114322 + (568+118)/117450 + (557+121)/120630 + (559+136)/123230 + (595+136)/127258)*100000
professor = ((229+39)/79620 + (238+33)/79369 + (156+33)/80815 + (174+55)/80636 + (200+51)/79407)*100000
lawyer = ((73+2)/20531 + (59+9)/22318 + (73+2)/24015 + (85+14)/25451 + (70+14)/27695)*100000
# (((4대 강력범죄 수) + (성범죄 수)) / (종사자 수))*100000

values = [doctor, lawyer, professor]
labels = ['의사', '변호사', '교수']


plt.figure(figsize=(5, 6))
plt.bar(labels, values, color=['green', 'green', 'green'])
plt.title('전문직 4대 강력범죄 현황')
# 살인·강도·절도·폭력·성폭력 기준
plt.xlabel('')
plt.ylabel('명')

plt.show()
# 단순 직종별 강력범죄자 수만 나타낸 그래프와 달리, 변호사와 교수의 순위가 바뀜. 성범죄자 수의 반영보다는 비율이 영향을 미친 듯?

''' 출처
전문직 4대 강력범죄 현황(살인·강도·절도·폭력 기준, 2015~2019년), 최근 5년간(2015~2019) 전문직 성범죄 현황(경찰청, 강병원 의원실)
https://www.chosun.com/national/welfare-medical/2021/02/27/KPO3GLYTN5GTTFIZS35PW2A7YY/

의사 수(통계청)
https://kosis.kr/statHtml/statHtml.do?sso=ok&returnurl=https%3A%2F%2Fkosis.kr%3A443%2FstatHtml%2FstatHtml.do%3Fconn_path%3DMT_RTITLE%26list_id%3DR_SUB_OTITLE_001_H03%26obj_var_id%3D%26seqNo%3D%26tblId%3DDT_2WH23080%26vw_cd%3DMT_RTITLE%26itm_id%3D%26language%3Dkor%26lang_mode%3Dko%26orgId%3D101%26

대학교 교원수(통계청, e-지방지표)
https://kosis.kr/statHtml/statHtml.do?sso=ok&returnurl=https%3A%2F%2Fkosis.kr%3A443%2FstatHtml%2FstatHtml.do%3Fconn_path%3DMT_GTITLE01%26list_id%3D104%26obj_var_id%3D%26seqNo%3D%26tblId%3DDT_1YL8901%26vw_cd%3DMT_GTITLE01%26itm_id%3D%26language%3Dkor%26lang_mode%3Dko%26orgId%3D101%26

2015.12.31 / 2016.12.31 / 2017.12.31 / 2018년 10월분 / 19.12.31 전국변호사현황(법무부)
https://www.moj.go.kr/bbs/moj/106/artclList.do
'''
