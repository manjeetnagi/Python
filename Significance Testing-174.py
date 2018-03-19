## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt
mean_group_a=np.mean(weight_lost_a)
mean_group_b=np.mean(weight_lost_b)
print(mean_group_a, mean_group_b)
plt.hist(weight_lost_a)
plt.show
plt.hist(weight_lost_b)
plt.show

## 4. Test statistic ##

mean_difference=mean_group_b-mean_group_a
print(mean_difference)

## 5. Permutation test ##

import numpy as np
import matplotlib.pyplot as plt


mean_differences=[]
for each in range(1000):
    group_a=[]
    group_b=[]
    for each in all_values:
        rand_num=np.random.rand(1,1)[0][0]
        if rand_num>=0.5:
            group_a.append(each)
        else:
            group_b.append(each)
    mean_a=np.mean(group_a)
    mean_b=np.mean(group_b)
    iteration_mean_difference=mean_b-mean_a
    mean_differences.append(iteration_mean_difference)
print(len(mean_differences))
plt.hist(mean_differences)

## 7. Dictionary representation of a distribution ##

sampling_distribution={}

for each in mean_differences:
    if sampling_distribution.get(each,False):
        sampling_distribution[each]+=1
    else:
        sampling_distribution[each]=1
print(sampling_distribution)

## 8. P value ##

frequencies=[]
obs=2.52
count=0
for each in sampling_distribution:
    if each >= obs:
        count+=1
p_value=count/1000
print(p_value)