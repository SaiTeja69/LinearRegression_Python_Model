features=[int(x) for x in input("Enter features").split()]
labels=[int(x) for x in input("Enter labels").split()]
def find_weight(labels,features):
    meandiff_num=0
    meandiff_den=0
    mean_i=sum(labels)/len(labels)
    mean_x=sum(features)/len(features)
    for i in range(len(labels)):
        meandiff_num=meandiff_num+(labels[i]-mean_i)*(features[i]-mean_x)
        meandiff_den=meandiff_den+(features[i]-mean_x)**2
    return meandiff_num/meandiff_den
def find_slope(weight,labels,features):
    slope=[]
    for i in range(len(labels)):
        z=labels[i]-features[i]*weight
        slope.append(z)
    return slope
def find_best_model(labels,features,weight,slope):
    pass
weight=find_weight(labels,features)
slope=find_slope(weight,labels,features)
print("y=",weight,"*x",slope[1])
