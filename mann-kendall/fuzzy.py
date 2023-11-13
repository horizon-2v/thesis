import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

# 设置变量范围
# 输入
x_stain_range = np.arange(1, 10, 0.01, np.float32)  # 输入1
x_oil_range = np.arange(1, 10, 0.01, np.float32)    # 输入2
# 输出
y_range = np.arange(1, 10, 0.01, np.float32)

# 创建模糊控制变量
x_stain = ctrl.Antecedent(x_stain_range, 'stain')      # 输入1
x_oil = ctrl.Antecedent(x_oil_range, 'oil')            # 输入2
y = ctrl.Consequent(y_range, 'powder')   # 输出

# 定义模糊集和其隶属度函数
x_stain.automf(3)  # 设置3个参考值，自动生成
# x_oil['poor'] = fuzz.gaussmf(x_oil_range, 1, 1)
# x_oil['average'] = fuzz.gaussmf(x_oil_range, 5.5, 1)
# x_oil['good'] = fuzz.gaussmf(x_oil_range, 10, 1)
x_oil.automf(3)
# 输出设置3个参考值
# y['N'] = fuzz.trapmf(y_range, [1, 1, 3, 4])
# y['M'] = fuzz.trapmf(y_range, [3, 4, 5, 6])
# y['P'] = fuzz.trapmf(y_range, [5, 6, 10, 10])
y['N'] = fuzz.gaussmf(x_oil_range, 1, 1)
y['M'] = fuzz.gaussmf(x_oil_range, 5.5, 1)
y['P'] = fuzz.gaussmf(x_oil_range, 10, 1)
# 参考值设置可视化
x_stain.view(), x_oil.view(), y.view()

# 设定输出的解模糊方法——质心解模糊方式
y.defuzzify_method = 'centroid'

# 输出为N的规则
rule0 = ctrl.Rule(antecedent=((x_stain['poor'] & x_oil['poor']) |
                              (x_stain['average'] & x_oil['poor'])),
                  consequent=y['N'], label='rule N')

# 输出为M的规则
rule1 = ctrl.Rule(antecedent=((x_stain['good'] & x_oil['poor']) |
                              (x_stain['poor'] & x_oil['average']) |
                              (x_stain['average'] & x_oil['average']) |
                              (x_stain['good'] & x_oil['good'])),
                  consequent=y['M'], label='rule M')

# 输出为P的规则
rule2 = ctrl.Rule(antecedent=((x_stain['average'] & x_oil['good']) |
                              (x_stain['good'] & x_oil['good'])),
                  consequent=y['P'], label='rule P')

# 规则设置可视化
rule0.view(), rule1.view(), rule2.view()

# 系统和运行环境初始化
system = ctrl.ControlSystem(rules=[rule0, rule1, rule2])
sim = ctrl.ControlSystemSimulation(system)

# 运行系统
sim.input['stain'] = 4
sim.input['oil'] = 7
sim.compute()
output_powder = sim.output['powder']

# 打印输出结果
print(output_powder)

# 画图y
y.view(sim=sim)
plt.show()
