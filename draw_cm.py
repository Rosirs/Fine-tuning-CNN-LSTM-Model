import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np
import seaborn as sns

# def draw_cm(cm_values):
    
#     plt.figure(figsize=(10, 7))
#     sns.heatmap(cm_values, annot=True, fmt=".1f", cmap="Blues")
#     plt.title('Confusion Matrix')
#     plt.xlabel('Predicted labels')
#     plt.ylabel('True labels')


#     plt.show()

def draw_cm(cm_values):
    # 混淆矩阵
    cm = cm_values
    # 计算行和列的总数
    total = sum(sum(cm))
    
    # 创建一个图形和子图
    plt.figure(figsize=(8, 8))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    
    # 绘制文本标签
    classes = [['True Positive', 'False Positive'],
               ['False Negative', 'True Negative']]
    tick_marks = [0, 1]
    classes_marks = ['Positive', 'Negative']
    plt.xticks(tick_marks, classes_marks, rotation=45, ha='right')
    plt.yticks(tick_marks, classes_marks)
    
    # 绘制矩阵中的值
    for i, j in np.ndindex(cm.shape):
        plt.text(j, i, f"{classes[i][j]}\n {float(cm[i, j])} \n ({cm[i, j]/total*100:.2f}%)", 
                 horizontalalignment="center",
                 color="black")  # 设置字体颜色为黑色
    
    # 添加轴标签
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
    # # 添加轴标签说明
    # plt.gcf().text(0.5, 0.04, 'Predicted label', ha='center')
    # plt.gcf().text(0.04, 0.5, 'True label', va='center', rotation='vertical')
    
    # 设置轴的显示范围
    plt.tight_layout()
    plt.savefig('confusion_matrix_CL_.png')
    # 显示图形
    plt.show()

cm_values = np.array([[44, 33],
                        [57, 77]])  # FN, TN
cm_values_ = np.array([[39, 37],
                [62, 73]])  # FN, TN

draw_cm(cm_values_)