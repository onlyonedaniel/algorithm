# algorithm

# 1.拉起项目
```shell
make build 
```

# 2. 进入容器中
```shell
docker-compose exec backend bash
```
# 3.在src/algorithm 下编写题目答案
    文件名以leetcode_编号_题目名称命名，一个题目可以写多种解题方法
  
  - 1.附上题目链接

  - 2.答案在leetcode 官网提交通过  

# 4.在src/Python/test 下编写测试用例
    函数以test 开头即可

# 5.代码格式化
```shell
make bi
``` 
# 6.测试
```shell
make test
```
