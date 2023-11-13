clear
clc
close all

% data = readmatrix('D:\workspace\Python\thesis\new_dataset\negative_data\000_1.csv'); 
data = readmatrix('D:\workspace\Python\thesis\new_dataset\positive_data\1.csv');
smoke_data = data(:,1);
CO_data = data(:,2);
temp_data = data(:,3);
data_length = length(smoke_data);
x = 1:166;

figure(1)
yyaxis left
p1 = plot(x,smoke_data,'-o');
xlabel('采样点数','fontsize',14);
ylabel('体积分数 ppm','fontsize',14);
hold on
p2 = plot(x,CO_data,'-*','MarkerIndices',1:5:length(CO_data),'MarkerFaceColor','b');
yyaxis right
p3 = plot(x, temp_data,'r-^','MarkerIndices',1:5:length(temp_data),'MarkerFaceColor','r');
ylabel('温度 ℃','fontsize',14)

set(gca,'fontsize',12)
grid minor;
hold off;
title('原始信号波形图','fontsize',14);
legend([p1, p2, p3],{'烟雾','CO','温度'},'fontsize',12,'Location','northwest')

figure(2)
f = imread('000_1grim.jpg');
imshow(f)
set(gca,'fontsize',24)
set(gca,'xtick',0:20:165);
set(gca,'ytick',0:20:165);
axis on
title('Grim变换信号特征图','fontsize',26);

figure(3)
imhist(f, 256);
set(gca,'fontsize',12)
grid minor;
title('Grim图片灰度直方图','fontsize',14);
axis([0,255,0,3000])





