clear all;
clc
t = [23,50,75,100,125,150];
pvc_b = [1.39,1.48,1.53,1.56,1.58,1.61];
xlpe_b = [1.29,1.35,1.41,1.47,1.53,1.59];
pvc_d = [0.235,0.232,0.223,0.21,0.19,0.192];
xlpe_d = [0.192,0.175,0.172,0.147,0.141,0.134];
figure(1)
p1 = plot(t,pvc_b);
hold on;
p2 = plot(t,xlpe_b);
set(gca,'fontsize',12)
grid minor;
title('比热变化曲线','fontsize',14);
xlabel('温度 ℃','fontsize',14);
ylabel('比热 kJ/(kg·K)','fontsize',14);
hold off;
legend([p1,p2],{'聚氯乙烯','交联聚乙烯'},'fontsize',12,'Location','southeast')

figure(2)
p1 = plot(t,pvc_d);
hold on;
p2 = plot(t,xlpe_d);
set(gca,'fontsize',12)
grid minor;
title('导热率变化曲线','fontsize',14);
xlabel('温度 ℃','fontsize',14);
ylabel('导热率 W/(m·K)','fontsize',14);
hold off;
legend([p1,p2],{'聚氯乙烯','交联聚乙烯'},'fontsize',12,'Location','northeast')
