clear
clc
close all
loss_func = readmatrix('D:\科研\学位论文\图\训练结果\误差函数\3-96-4.csv');
loss_func = smooth(loss_func(:,3), 0.6);
acc = readmatrix('D:\科研\学位论文\图\训练结果\准确率\3-96-4.csv');
acc = smooth(acc(:,3),0.6);

figure(1)
yyaxis left
p1 = plot(loss_func,'-o','MarkerFaceColor','b');
xlabel('训练轮次','fontsize',14);
ylabel('验证误差','fontsize',14);
hold on
yyaxis right
p2 = plot(acc,'r-^','MarkerFaceColor','r');
ylabel('准确率','fontsize',14)

set(gca,'fontsize',12)
grid minor;
hold off;
title('验证误差与准确率曲线','fontsize',14);
legend([p1, p2],{'损失函数','准确率'},'fontsize',12,'Location','southeast')


function [smooth_data] = smooth(data,weight)
    smooth_data = zeros(length(data),1);
    last = data(1);
    for i = 1:length(data)
        smooth_data(i) = weight*last + (1-weight)*data(i);
        last = smooth_data(i);
    end
end

