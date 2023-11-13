clear
clc
temp_true = [19.106509962938958, 17.980685878495464, 14.768851650432437, 10.512473073416734, -1.2037396106914486, 6.024283852114744]; 
temp_false = [-1.2819407918964614, 1.382485167731478, -0.2541538389162919, 0.5669585637363435, -0.4887573825313306, 0.921656778487652];
smoke_true = [14.615566064545694, 0.3016331275050497, 9.685774872106597, 4.220070885741946, 0.016757395972502764, 3.2034555300767784];
smoke_false = [-1.0892307382126796, -0.36586981206631036, 1.8684496509340582, 0.9132780805014006, 1.3992425637039807, 0.6228165503113527];
CO_true = [11.092226018764755, 8.699881409057685, 0.6814674362151124, 9.412070737889053, -0.6996219640088072, 3.566532442814338];
CO_false = [0.10054437583501659, -2.013680416029082, 0.2597396375737928, -0.5250650738050866, -0.7568757180913749, 2.4158579193691483];

t = [10, 20, 30, 40, 50, 60];

figure(1)
p1 = plot(t,smoke_true,'V-','MarkerFaceColor','b');
hold on;
p2 = plot(t,smoke_false,'s-','MarkerFaceColor','r');

set(gca,'fontsize',12)
grid minor;
title('烟雾传感器Mann-Kendall趋势对比图','fontsize',14);
xlabel('时间 s','fontsize',14);
ylabel('Z值','fontsize',14);
hold off;
legend([p1, p2],{'传感器','噪声'},'fontsize',12,'Location','northeast')

figure(2)
p1 = plot(t,CO_true,'V-','MarkerFaceColor','b');
hold on;
p2 = plot(t,CO_false,'s-','MarkerFaceColor','r');

set(gca,'fontsize',12)
grid minor;
title('CO传感器Mann-Kendall趋势对比图','fontsize',14);
xlabel('时间 s','fontsize',14);
ylabel('Z值','fontsize',14);
hold off;
legend([p1, p2],{'传感器','噪声'},'fontsize',12,'Location','northeast')
