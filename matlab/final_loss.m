clear;
clc;
close all;

data = readmatrix('D:\科研\学位论文\图\逆瓶颈优化\损失函数\3-96-4.csv');
epochs = data(:,2);
ConvNeXt_T = smooth(data(:,3),0.6);

data = readmatrix('D:\科研\学位论文\图\逆瓶颈优化\损失函数\1-24-4.csv');
ConvNeXt_24 = smooth(data(:,3),0.6);

data = readmatrix('D:\科研\学位论文\图\逆瓶颈优化\损失函数\1-24-2.csv');
ConvNeXt_FiRe = smooth(data(:,3),0.6);

figure(1)
p1 = plot(epochs,ConvNeXt_T,'r-o','MarkerFaceColor','r');
hold on;
p2 = plot(epochs,ConvNeXt_24,'g-^','MarkerFaceColor','g');
p3 = plot(epochs,ConvNeXt_FiRe,'b-p','MarkerFaceColor','b');

set(gca,'fontsize',12)
grid minor;
title('逆瓶颈结构优化模型损失函数实验','fontsize',14);
xlabel('训练轮次','fontsize',14);
ylabel('损失函数值','fontsize',14);
hold off;
legend([p1, p2, p3],{'ConvNeXt-T','逆瓶颈24通道','半逆瓶颈24通道'},'fontsize',12,'Location','northeast')

function [smooth_data] = smooth(data,weight)
    smooth_data = zeros(length(data),1);
    last = data(1);
    for i = 1:length(data)
        smooth_data(i) = weight*last + (1-weight)*data(i);
        last = smooth_data(i);
    end
end
