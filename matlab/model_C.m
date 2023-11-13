clear
clc
data = xlsread('D:\科研\学位论文\图\4-2-2\仿真结果\传感器仿真结果.xlsx', 'Sheet1');	
t = data(:,1);
smoke_data = data(:,2:3:14);

figure(1)
p1 = plot(t,10e6*smoke_data(:,1));
hold on;
p2 = plot(t,10e6*smoke_data(:,2));
p3 = plot(t,10e6*smoke_data(:,3));
p4 = plot(t,10e6*smoke_data(:,4));
p5 = plot(t,10e6*smoke_data(:,5));

set(gca,'fontsize',12)
grid minor;
title('建模场景C烟雾传感器信号波形图','fontsize',14);
xlabel('时间 s','fontsize',14);
ylabel('体积分数 ppm','fontsize',14);
hold off;
legend([p1, p2, p3, p4, p5],{'仿真2','仿真6','仿真9','仿真10', '仿真11'},'fontsize',12,'Location','northwest')

CO_data = data(:,3:3:15);
figure(2)
p1 = plot(t,10e6*CO_data(:,1));
hold on;
p2 = plot(t,10e6*CO_data(:,2));
p3 = plot(t,10e6*CO_data(:,3));
p4 = plot(t,10e6*CO_data(:,4));
p5 = plot(t,10e6*CO_data(:,5));

set(gca,'fontsize',12)
grid minor;
title('建模场景C一氧化碳传感器信号波形图','fontsize',14);
xlabel('时间 s','fontsize',14);
ylabel('体积分数 ppm','fontsize',14);
hold off;
legend([p1, p2, p3, p4, p5],{'仿真2','仿真6','仿真9','仿真10', '仿真11'},'fontsize',12,'Location','northwest')

TEMP_data = data(:,4:3:16);
figure(3)
p1 = plot(t,TEMP_data(:,1));
hold on;
p2 = plot(t,TEMP_data(:,2));
p3 = plot(t,TEMP_data(:,3));
p4 = plot(t,TEMP_data(:,4));
p5 = plot(t,TEMP_data(:,5));


set(gca,'fontsize',12)
grid minor;
title('建模场景C温度传感器信号波形图','fontsize',14);
xlabel('时间 s','fontsize',14);
ylabel('温度 ℃','fontsize',14);
hold off;
legend([p1, p2, p3, p4, p5],{'仿真2','仿真6','仿真9','仿真10', '仿真11'},'fontsize',12,'Location','northwest')