#coding:utf-8

"""
Operation redis module
"""
import redis

pool = redis.ConnectionPool(host="192.168.2.41", port="6379")
r = redis.Redis(connection_pool=pool)

#1 String 操作,redis中的String在在内存中按照一个name对应一个value来存储
r.set("name","zhangsan")
r.setex("name","zhangsan",10)# 设置过期时间(秒)
r.psetex("name",1000,"zhangsan")# 设置过期时间(毫秒)
r.mset(name1="zhangsan",name2="lisi")# 批量设置
print r.mget("name1","name2")# 批量获取
print r.getset("name1","wangwu")# 设置新值,打印原值
print r.get("name1")
r.set("name","zhangsan")
print r.getrange("name",0,3)# 获取子序列
r.setrange("name",1,"z")# 修改字符串内容，从指定字符串索引开始向后替换，如果新值太长时，则向后添加
print r.get("name")
r.setrange("name",6,"zzzzzzz")
print r.get("name")
r.setbit("n1",1000,1) #设置第1000bit位的值为1，使用ord,bin查看,r.setbit()
r.getbit("n1",1000) #获取第1000bit位的值
r.bitcount("n1") #统计bit位上为1的个数
"""
注：如果在Redis中有一个对应： n1 = "foo"，那么字符串foo的二进制表示为：01100110 01101111 01101111所以，如果执行 setbit('n1', 7, 1)，则就会将第7位设置为1，
    那么最终二进制则变成 01100111 01101111 01101111，即："goo
"""


#2 Hash 操作redis中的Hash 在内存中类似于一个name对应一个dic来存储
r.hset("dic_name","name","James")# name对应的hash中设置一个键值对（不存在，则创建，否则，修改）
print r.hget("dic_name","name")
print r.hgetall("dic_name")
r.hmset("dic_name",{"name":"James","age":23})
print r.hget("dic_name","age")
print r.hmget("dic_name","name","age")# 在name对应的hash中获取多个key的值
print r.hlen("dic_name")#hlen(name) 获取hash中键值对的个数
print r.hkeys("dic_name")#hkeys(name) 获取hash中所有的key的值
print r.hvals("dic_name")#hvals(name) 获取hash中所有的value的值
print r.hexists("dic_name","name")#检查name对应的hash是否存在当前传入的key
r.hdel("dic_name","name")#删除指定name对应的key所在的键值对
r.hincrby("demo","a",amount=2)#自增hash中key对应的值，不存在则创建key=amount(amount为整数)


#3、List 操作redis中的List在在内存中按照一个name对应一个List来存储
r.lpush("list_name",2)#在name对应的list中添加元素，每个新的元素都添加到列表的最左边
r.lpush("list_name",3,4,5)#保存在列表中的顺序为5，4，3，2
print r.llen("list_name")#name对应的list元素的个数
r.linsert("list_name","BEFORE","2","SS")#在列表内找到第一个元素2，在它前面插入SS
r.lset("list_name",0,"bbb")#对list中的某一个索引位置重新赋值
r.lrem("list_name","SS",num=0)#删除name对应的list中的指定值
r.lpop("list_name")#移除列表的左侧第一个元素，返回值则是第一个元素
print r.lindex("list_name",1)#根据索引获取列表内元素
print r.lrange("list_name",0,-1)#分片获取元素
r.ltrim("list_name",0,2)#移除列表内没有在该索引之内的值


#4、Set 操作Set集合就是不允许重复的列表
r.sadd("set_name","aa")
r.sadd("set_name","aa","bb")
print r.smembers("set_name")#获取name对应的集合的所有成员
print r.scard("set_name")#获取name对应的集合中的元素个数
r.sadd("set_name","aa","bb")
r.sadd("set_name1","bb","cc")
r.sadd("set_name2","bb","cc","dd")
print r.sdiff("set_name","set_name1","set_name2")#在第一个name对应的集合中且不在其他name对应的集合的元素集合
print r.sinter("set_name","set_name1","set_name2")# 获取多个name对应集合的交集
print r.sismember("set_name","aa")#检查value是否是name对应的集合内的元素
r.smove("set_name","set_name1","aa")#将某个元素从一个集合中移动到另外一个集合
r.spop("bb")#从集合的右侧移除一个元素，并将其返回
print r.srandmember("set_name2",2)# 从name对应的集合中随机获取numbers个元素
r.srem("set_name2","bb","dd")#删除name对应的集合中的某些值
r.sunion("set_name","set_name1","set_name2")#获取多个name对应的集合的并集


