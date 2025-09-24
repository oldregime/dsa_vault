import java.util.ArrayList;

public class ArrayListe {
	public static void main (String[] Args)
	{
		ArrayList<String> name = new ArrayList<>(); // Simplified generic instantiation
		name.add("hello");
		name.add("world");
		name.add("b");
		name.add(1,"bye");
		System.out.println(name.size());
		System.out.println(name.get(2));

		System.out.println(name);
		name.remove(0);
		name.remove("b");
		name.set(0,"gfg");


		System.out.println(name);
		boolean check = name.isEmpty();
		System.out.println(check);



		ArrayList<String> nam1 = new ArrayList<>(); // Simplified generic instantiation
		nam1.add("asdasd");
		nam1.add("asdasddq");
		nam1.add("123d1f");
		System.out.println(nam1);
		name.addAll(nam1);
		System.out.println(nam1);
		System.out.println(name);






	}
}

