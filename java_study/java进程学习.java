public class javaStudy implements Runnable{

	public static void main(String[] args) {
		javaStudy t1 = new javaStudy();
		Thread ta = new Thread(t1,"A");
		Thread tb = new Thread(t1,"B");
		ta.start();
		tb.start();
	}
	
	@Override
	public void run() {
		// TODO Auto-generated method stub
		for(int i=0;i<5;i++){
			System.out.println(Thread.currentThread().getName()+"synchronized loop"+i);
		}
	}
	
}

线程和进程一样分为5个阶段：创建、就绪、运行、阻塞、终止
多进程是指操作系统能同时运行多个任务（程序）
多线程是指在同一程序中有多个顺序流在执行

在java中要想实现多线程，有两种手段，一种是继续Thread类，另外一种是实现Runable接口.
(其实准确来讲，应该有三种，还有一种是实现Callable接口，并与Future、线程池结合使用)

方法一：扩展java.lang.Thread类
这里继承Thread类的方法是比较常用的一种，如果说你只是想起一条线程。没有什么其它特殊的要求，那么可以使用Thread

package experiment;

public class ThreadStudy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread1 mth1 = new Thread1("A");
		Thread1 mth2 = new Thread1("B");
		mth1.start();
		mth2.start();
	}
}
class Thread1 extends Thread{
	private String name;
	public Thread1(String name){
		this.name = name;
	}
	public void run(){
		for(int i=0;i<5;i++){
			System.out.println(name+"运行 ："+i);
			try{
				sleep(1000);
			}catch(InterruptedException e){
				e.printStackTrace();
			}
		}
	}
}
程序启动运行main时候，java虚拟机启动一个进程，主线程main在main()调用时候被创建。
随着调用Thread1的两个对象的start方法，另外两个线程也启动了，这样，整个应用就在多线程下运行。
注意：start()方法的调用后并不是立即执行多线程代码，而是使得该线程变为可运行态（Runnable），什么时候运行是由操作系统决定的。
从程序运行的结果可以发现，多线程程序是乱序执行。因此，只有乱序执行的代码才有必要设计为多线程。
Thread.sleep()方法调用目的是不让当前线程独自霸占该进程所获取的CPU资源，以留出一定时间给其他线程执行的机会。
实际上所有的多线程代码执行顺序都是不确定的，每次执行的结果都是随机的。

output：
A运行 ：0
B运行 ：0
A运行 ：1
B运行 ：1
A运行 ：2
B运行 ：2
A运行 ：3
B运行 ：3
A运行 ：4
B运行 ：4

方法二：实现java.lang.Runnable接口
采用Runnable也是非常常见的一种，我们只需要重写run方法即可
public class RunnableStudy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new thread2("A")).start();
		new Thread(new thread2("B")).start();
	}

}

class thread2 implements Runnable{
	public String name;
	
	public thread2(String name){
		this.name = name;
	}
	
	@Override
	public void run() {
		// TODO Auto-generated method stub
		for(int i=0;i<5;i++){
			System.out.println(name +"运行"+i);
			try{
				Thread.sleep(1000);
			}catch(InterruptedException e){
				e.printStackTrace();
			}
		}
	}
output：
A运行0
B运行0
A运行1
B运行1
A运行2
B运行2
A运行3
B运行3
A运行4
B运行4

Thread2类通过实现Runnable接口，使得该类有了多线程类的特征。run（）方法是多线程程序的一个约定。
所有的多线程代码都在run方法里面。Thread类实际上也是实现了Runnable接口的类。在启动的多线程的时候，
需要先通过Thread类的构造方法Thread(Runnable target) 构造出对象，然后调用Thread对象的start()方法来运行多线程代码。
实际上所有的多线程代码都是通过运行Thread的start()方法来运行的。因此，不管是扩展Thread类还是实现Runnable接口来实现多线程，
最终还是通过Thread的对象的API来控制线程的，熟悉Thread类的API是进行多线程编程的基础。

三、Thread和Runnable的区别
如果一个类继承Thread，则不适合资源共享。但是如果实现了Runable接口的话，则很容易的实现资源共享。
总结：
实现Runnable接口比继承Thread类所具有的优势：
1）：适合多个相同的程序代码的线程去处理同一个资源
2）：可以避免java中的单继承的限制
3）：增加程序的健壮性，代码可以被多个线程共享，代码和数据独立
4）：线程池只能放入实现Runable或callable类线程，不能直接放入继承Thread的类

public class RunnableStudy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		thread2 mthd = new thread2("A");
		new Thread(mthd).start();
		new Thread(mthd).start();
	}
}
class thread2 implements Runnable{
	public String name;
	private int count=15;
	
	public thread2(String name){
		this.name = name;
	}
	
	@Override
	public void run() {
		// TODO Auto-generated method stub
		for(int i=0;i<5;i++){
			System.out.println(name +"运行"+count--);
			try{
				Thread.sleep(1000);
			}catch(InterruptedException e){
				e.printStackTrace();
			}
		}
	}
}
output:
		A运行15
		A运行14
		A运行13
		A运行12
		A运行11
		A运行10
		A运行9
		A运行8
		A运行7
		A运行6
		
public class ThreadStudy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread1 mth1 = new Thread1("A");
		Thread1 mth2 = new Thread1("B");
		mth1.start();
		mth2.start();
	}
}

class Thread1 extends Thread{
	private String name;
	private int count = 15;
	public Thread1(String name){
		this.name = name;
	}
	public void run(){
		for(int i=0;i<5;i++){
			System.out.println(name+"运行 ："+count--);
			try{
				sleep(1000);
			}catch(InterruptedException e){
				e.printStackTrace();
			}
		}
	}
}
output：
		A运行 ：15
		B运行 ：15
		A运行 ：14
		B运行 ：14
		A运行 ：13
		B运行 ：13
		B运行 ：12
		A运行 ：12
		B运行 ：11
		A运行 ：11

		提醒一下大家：main方法其实也是一个线程。在java中所有的线程都是同时启动的，至于什么时候，哪个先执行，完全看谁先得到CPU的资源。
在java中，每次程序运行至少启动2个线程。一个是main线程，一个是垃圾收集线程。因为每当使用java命令执行一个类的时候，实际上都会启动一个jvm，
每一个jvm实际上就是在操作系统中启动了一个进程。

