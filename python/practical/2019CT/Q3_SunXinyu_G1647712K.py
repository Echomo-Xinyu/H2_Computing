# Task 3.1
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList():
    def __init__(self):
        self.start = None
    def insert(self, data):
        newNode = Node(data)
        if self.start == None:
            self.start = newNode
        else:
            newNode.next = self.start
            self.start = newNode
    def delete(self, data):
        if self.start == None:
            return False
        currentNode = self.start
        if currentNode.data == data:
            self.start = self.start.next
            return True
        while currentNode.next and currentNode.next.data!=data:
            currentNode = currentNode.next
        if currentNode.next == None:
            return False
        else:
            currentNode.next = currentNode.next.next
            return True
    def exists(self, data):
        if self.start == None:
            return True
        currentNode = self.start
        while currentNode and currentNode.data!=data:
            currentNode = currentNode.next
        return currentNode.data == data
    def print(self):
        if self.start == None:
            print("[]")
            return
        currentNode = self.start
        print("[", end="")
        while currentNode:
            if currentNode is not self.start:
                print(";", end="")
            print(str(currentNode.data), end="")
            currentNode = currentNode.next
        print("]", end="")

# Task 3.2
ll = LinkList()
ll.insert("ABC")
ll.insert(2)
ll.insert(1)
ll.delete(1)
ll.print()

print()

# Task 3.3
class Post():
    def __init__(self, title, content):
        self.title = title
        self.content = content
    def __str__(self):
        return self.title + ":" + self.content

class HashTable():
    def __init__(self, size):
        self._array = [None for i in range(size)]
        self._size = size
    def _hash(self, string):
        return hash(string)%self._size
    def insert(self, title, Post):
        hash_value = self._hash(title)
        if self._array[hash_value] == None:
            self._array[hash_value] = Post
            return True
        index_now = (hash_value + 1) % self._size
        while index_now != hash_value:
            if self._array[index_now] == None:
                self._array[index_now] = Post
                return True
            index_now = (index_now + 1) % self._size
        return False
    def getValue(self, title):
        hash_value = self._hash(title)
        if self._array[hash_value].title == title:
            return self._array[hash_value]
        index_now = (hash_value + 1) % self._size
        while index_now != hash_value:
            if self._array[index_now].title == title:
                return self._array[index_now]
            index_now = (index_now + 1) % self._size
        return None

# Task 3.4
ht = HashTable(10)
post1 = Post("test1", "This is a test")
post2 = Post("number2", "Another test")
ht.insert(post1.title, post1)
ht.insert(post2.title, post2)
print(str(ht.getValue("test1")))
print(str(ht.getValue("number2")))

# Task 3.5
class User():
    def __init__(self, name, sub_type):
        self.name = name
        self._friends = LinkList()
        subscription_type = {"trial":10, "basic":100, "premier":1000}
        self._posts = HashTable(subscription_type[sub_type])
    def getFriends(self):
        return self._friends
    def addFriend(self, another_user):
        self._friends.insert(another_user)
        another_user._friends.insert(self)
    def unfriend(self, another_user):
        self._friends.delete(another_user)
        another_user._friends.delete(self)
    def isFriend(self, another_user):
        return self._friends.exists(another_user)
    def showFriends(self):
        print(self.name + "\'s friends:", end="")
        self._friends.print()
        print()
    def addPost(self, Post):
        if self._posts.insert(Post.title, Post):
            return
        else:
            print("Maximum limit of posts exceeded.")
    def getTitles(self):
        title_arr = []
        for i in range(len(self._posts)):
            # comment to avoid the error
            # if self._posts[i]!=None:
            #     title_arr.append(self._posts[i].title)
            print(i)
        return title_arr
    def getPosts(self, title):
        return self._posts.getValue(title)
    def __str__(self):
        return self.name

# Task 3.6
john = User("John", "trial")
mary = User("Mary", "basic")
alan = User("Alan", "premier")
john.addFriend(mary)
john.addFriend(alan)
john.showFriends()
mary.showFriends()
alan.unfriend(john)
john.showFriends()
































        
