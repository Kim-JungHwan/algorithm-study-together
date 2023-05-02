#include<iostream>
#include<string>

using namespace std;

// 연결리스트 노드
struct Node
{
    int data; 
    Node* next; // 다음 노드를 가리키는 포인터

    // 구조체 생성자
    Node(int element)
    {
        data = element;
        next = nullptr;
    }
};

class Queue {
public:
    Node* front;
    Node* back;
    int size; // 큐의 크기

    Queue()
    {
        front = nullptr;
        back = nullptr;
        size = 0;
    }

    int Empty()
    {
        if (front == nullptr)
            return 1;
        else
            return 0;
    }

    void Push(int element)
    {
        Node* newNode = new Node(element); // 새로운 노드 생성
        // 처음 생성 시
        if (Empty() == 1)
        {
            // front와 back 인덱스 모두 같은 노드를 가리킨다.
            front = newNode;
            back = newNode;
        }
        else
        {
            // 새로운 노드를 맨 뒤에서부터 넣는다.
            back->next = newNode; // back의 next 포인터가 newNode를 가리키게 한다.
            back = newNode; // back의 포인터가 newNode를 가리키게 한다.
        }
        size++;

    }

    int Pop()
    {
        if (Empty() == 1)
        {
            return -1;
        }
        int element = front->data; // 맨 앞에 있는 데이터 꺼내기
        Node* temp = front;
        front = front->next;
        delete temp;
        if (front == nullptr)
        {
            back = nullptr;
        }
        size--;
        return element;
    }

    int Size()
    {
        return size;
    }

    int Front()
    {
        if (front == nullptr)
        {
            return -1;
        }
        else
            return front->data;
    }

    int Back()
    {
        if (back == nullptr)
        {
            return -1;
        }
        else
            return back->data;
    }
    
};

int main()
{    
    // 입출력속도 개선
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    Queue queue; // 큐 생성
    int n; // 명령의 수         
    string inputStr; // 입력받는 문자열
    string cmd; // 명령어

    cin >> n;
    cin.ignore();  // 버퍼 비우기
    
    while (n > 0)
    {        
        cin >> inputStr;

        if (inputStr == "push")
        {
            int element; // push 명령으로 입력받는 정수   
            cin >> element;            
            // push 명령 실행
            queue.Push(element);
        }
        else if (inputStr == "pop")
        {
            // pop 명령 실행, 출력
            cout << queue.Pop() << '\n';
        }
        else if (inputStr == "size")
        {
            cout << queue.Size() << '\n';
        }
        else if (inputStr == "empty")
        {
            cout << queue.Empty() << '\n';
        }
        else if (inputStr == "front")
        {
            cout << queue.Front() << '\n';
        }
        else if (inputStr == "back")
        {
            cout << queue.Back() << '\n';
        }

        n--;
    }

    return 0;
}