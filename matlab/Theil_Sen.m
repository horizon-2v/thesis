clear
clc
temp_true = [0.00011448193588552742, 0.0074817399281297894, 0.0032252160352284074, 0.001957648700412423, -6.16209545751111e-05, 0.0009367853497366911]; 
temp_false = [0.004166551082627173, 0.000283406457648637, 0.0023076914086287664, -6.795498122159712e-05, 0.0009530581033304126, 0.0034653549935034222];
smoke_true =[4.150377473583922e-06, 0.00013519680487888834, 0.003254808449611414, 0.002025609279299708, 6.693383069597229e-06, 0.0018310081797671444];
smoke_false = [-0.003835193948054078, 0.0008915060233478429, 8.423463019339209e-05, 0.0030338982917996814, -0.0009042263929086888, 1.5830532211079846e-05];
CO_true = [0.0, 0.004185925559926224, 0.0002404926022695278, 0.005013377717563831, -0.0004846690380612574, 0.0012955528474153377];
CO_false = [-9.71133285448238e-05, 0.0007929506735565623, 0.0013543640578261317, -0.00038539634951782807, 0.0023539828699006213, 0.002007029301986067];

t = [10, 20, 30, 40, 50, 60];

figure(1)
p1 = plot(t,smoke_true,'V-','MarkerFaceColor','b');
hold on;
p2 = plot(t,smoke_false,'s-','MarkerFaceColor','r');

set(gca,'fontsize',12)
grid minor;
title('烟雾传感器Theil-Sen斜率对比图','fontsize',14);
xlabel('时间 s','fontsize',14);
ylabel('斜率k','fontsize',14);
hold off;
legend([p1, p2],{'传感器','噪声'},'fontsize',12,'Location','northeast')

figure(2)
p1 = plot(t,CO_true,'V-','MarkerFaceColor','b');
hold on;
p2 = plot(t,CO_false,'s-','MarkerFaceColor','r');

set(gca,'fontsize',12)
grid minor;
title('CO传感器Theil-Sen斜率对比图','fontsize',14);
xlabel('时间 s','fontsize',14);
ylabel('斜率k','fontsize',14);
hold off;
legend([p1, p2],{'传感器','噪声'},'fontsize',12,'Location','northeast')


figure(3)
p1 = plot(t,temp_true,'V-','MarkerFaceColor','b');
hold on;
p2 = plot(t,temp_false,'s-','MarkerFaceColor','r');

set(gca,'fontsize',12)
grid minor;
title('温度传感器Theil-Sen斜率对比图','fontsize',14);
xlabel('时间 s','fontsize',14);
ylabel('斜率k','fontsize',14);
hold off;
legend([p1, p2],{'传感器','噪声'},'fontsize',12,'Location','northeast')
