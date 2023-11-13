clear
clc
data = csvread("D:\workspace\Python\mann-kendall\SG_filter.csv",1,1);
original_data = data(:,1);
smooth_data = data(:,2);
t = xlsread('D:\科研\学位论文\图\3-2-2\仿真结果\传感器仿真.xlsx', 'Sheet1'); 
t = t(:,1);

figure(1)
p1 = plot(t,original_data,'b-');
hold on;
p2 = plot(t,smooth_data,'r-');

set(gca,'fontsize',12)
grid minor;
title('SG滤波结果图','fontsize',14);
xlabel('时间 s','fontsize',14);
ylabel('体积分数 mol/mol','fontsize',14);
hold off;
legend([p1, p2],{'源数据','滤波后数据'},'fontsize',12,'Location','southeast')