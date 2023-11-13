clear;
clc;
close all;
data = readmatrix('D:\科研\学位论文\图\模型对比\准确率\ConvNeXt-FiRe.csv');
epochs = data(:,2);
ConvNeXt_FiRe = smooth(data(:,3),0.6);

data = readmatrix('D:\科研\学位论文\图\训练结果\准确率\3-96-4.csv');
ConvNeXt_T = smooth(data(:,3),0.6);

figure(1)
p1 = plot(epochs,ConvNeXt_FiRe,'r-o','MarkerFaceColor','r');
hold on;
p2 = plot(epochs,ConvNeXt_T,'b-^','MarkerFaceColor','b');

set(gca,'fontsize',12)
grid minor;
title('自定义数据集模型训练准确率','fontsize',14);
xlabel('训练轮次','fontsize',14);
ylabel('准确率','fontsize',14);
hold off;
legend([p1, p2],{'ConvNeXt-FiRe','ConvNeXt-T'},'fontsize',12,'Location','southeast')

function [smooth_data] = smooth(data,weight)
    smooth_data = zeros(length(data),1);
    last = data(1);
    for i = 1:length(data)
        smooth_data(i) = weight*last + (1-weight)*data(i);
        last = smooth_data(i);
    end
end
