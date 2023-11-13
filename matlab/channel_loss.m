clear;
clc;
close all;

data = readmatrix('D:\科研\学位论文\图\通道优化\损失函数\1-96-4.csv');
epochs = data(:,2);
jiuliu_ch = smooth(data(:,3),0.6);

data = readmatrix('D:\科研\学位论文\图\通道优化\损失函数\1-64-4.csv');
liusi_ch = smooth(data(:,3),0.6);

data = readmatrix('D:\科研\学位论文\图\通道优化\损失函数\1-48-4.csv');
siba_ch = smooth(data(:,3),0.6);

data = readmatrix('D:\科研\学位论文\图\通道优化\损失函数\1-32-4.csv');
saner_ch = smooth(data(:,3),0.6);

data = readmatrix('D:\科研\学位论文\图\通道优化\损失函数\1-24-4.csv');
ersi_ch = smooth(data(:,3),0.6);

figure(1)
p1 = plot(epochs,jiuliu_ch,'r-o','MarkerFaceColor','r');
hold on;
p2 = plot(epochs,liusi_ch,'g-^','MarkerFaceColor','g');
p3 = plot(epochs,siba_ch,'b-p','MarkerFaceColor','b');
p4 = plot(epochs,saner_ch,'m-d','MarkerFaceColor','m');
p5 = plot(epochs,ersi_ch,'c-s','MarkerFaceColor','c');

set(gca,'fontsize',12)
grid minor;
title('不同通道数模型训练损失函数','fontsize',14);
xlabel('训练轮次','fontsize',14);
ylabel('损失函数值','fontsize',14);
hold off;
legend([p1, p2, p3, p4, p5],{'ConvNeXt-96','ConvNeXt-64','ConvNeXt-48','ConvNeXt-32','ConvNeXt-24'},'fontsize',12,'Location','northeast')

function [smooth_data] = smooth(data,weight)
    smooth_data = zeros(length(data),1);
    last = data(1);
    for i = 1:length(data)
        smooth_data(i) = weight*last + (1-weight)*data(i);
        last = smooth_data(i);
    end
end
