import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class test {

	public void jesus() {
		String time = "10:05";
		String s[] = time.split(":");
		time.split(":");
		System.out.println(time);
		int minutes = (Integer.parseInt(s[0]) * 60) + Integer.parseInt(s[1]);

		List<Integer> list = new ArrayList<Integer>();

		list.add(1);
		list.add(23);
		list.add(69);
		list.add(203);
		list.add(1231231);
		list.add(-111);

		Collections.sort(list);
		Collections.reverse(list);

		int right = list.size() - 1;

		System.out.println(list);

		for (int i = 0; i < list.size(); i++) {
			while (right != i) {
				right--;
				list.remove(Math.max(list.get(i),list.get(right)));
			}
		}

		System.out.println("Time in HH:MM " + time);
		System.out.println("Time in MM " + minutes);
	}
	public static int amount = 35, tamount = amount;
	public static void createPeople() throws InterruptedException {
		Random rand = new Random();
		String names[] = {"Eddie", "Soland", "Paul", "Mike", "David", "DC"};
		while(amount > 0) {
			Thread.sleep(1000);
			WebDriver driver = new ChromeDriver();
			driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd4q05reJjiGNKFqWBXXeF5ZgtDzXhv9YdnvIuIJ3Zk1ldBVQ/viewform");
			for(int j =1; j < 17; j++) {
				driver.findElement(By.xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div["+j+"]/div/div/div[2]/div/div[1]/div/div[1]/input")).sendKeys(names[rand.nextInt(names.length-1)]);
			}
			driver.findElement(By.xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div[1]/div/div[1]/input")).sendKeys(names[rand.nextInt(names.length)]+" and "+names[rand.nextInt(names.length)]);
			driver.findElement(By.xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div")).click();
			driver.findElement(By.xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span")).click();
			amount--;
			driver.close();
			System.out.println("["+amount+"] out of ["+tamount+"]");
		}	
	}
	public static void main(String[] args) throws InterruptedException {
		
		System.setProperty("webdriver.chrome.driver", "chromedriver");
		for(int i = 0; i < 4; i++) {
			Thread thread = new Thread() {
				public void run() {
					try {
						createPeople();
					} catch (InterruptedException e) {
						e.printStackTrace();
					}		
				}
			};
			thread.start();
			System.out.println("Thread "+i+" started");
		}
	}
}