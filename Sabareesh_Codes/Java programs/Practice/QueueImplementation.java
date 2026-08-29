// Java Program: Queue Implementation using Array
// Date: 2026-08-29

package Practice;

public class QueueImplementation {
    private int capacity;
    private int[] queue;
    private int front, rear, size;

    public QueueImplementation(int capacity) {
        this.capacity = capacity;
        this.queue = new int[capacity];
        this.front = 0;
        this.rear = -1;
        this.size = 0;
    }

    public void enqueue(int item) {
        if (size == capacity) {
            System.out.println("Queue is full!");
            return;
        }
        rear = (rear + 1) % capacity;
        queue[rear] = item;
        size++;
    }

    public int dequeue() {
        if (size == 0) {
            System.out.println("Queue is empty!");
            return -1;
        }
        int item = queue[front];
        front = (front + 1) % capacity;
        size--;
        return item;
    }

    public static void main(String[] args) {
        QueueImplementation q = new QueueImplementation(5);
        q.enqueue(10);
        q.enqueue(20);
        q.enqueue(30);
        System.out.println("Dequeued: " + q.dequeue());
        System.out.println("Dequeued: " + q.dequeue());
    }
}
