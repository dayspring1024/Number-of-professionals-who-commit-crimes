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
plt.title('전문직 5대 강력범죄 현황') # 살인·강도·절도·폭력·성폭력 기준
plt.xlabel('')
plt.ylabel('명')

plt.show()
