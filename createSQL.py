
a=[2,5,3,64,24,7,8]
maxe=3
page=4
page = max(1,page)
if int(len(a)) < (int(page)-1)*maxe:
    page-=1
print(a[int(page-1)*(maxe):int(page)*maxe])
