clear all;
clc
x = 0:150;
y = 0.04698*power(x,2);
fig_x = 0:199;
fig_y = 0.04698*150*150*ones(1,200);
fig_y(1:151) = y;
figure(1)
p1 = plot(fig_x,fig_y);
hold on;
p2 = plot(fig_x(151),fig_y(151),'O','color','r');
set(gca,'fontsize',12)
grid minor;
title('热释放速率曲线','fontsize',14);
xlabel('时间 s','fontsize',14);
ylabel('热释放速率 kW/s^2','fontsize',14);
hold off;
legend(p1,'热释放速率','fontsize',12,'Location','southeast')
text(fig_x(151)-20,fig_y(151)+50,'Q_{max}=1051.05kJ','fontsize',12);
