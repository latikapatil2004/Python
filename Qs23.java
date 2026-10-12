class Qs1
{
	public static void main(String[]args)
	{
		int arr[]={1,2,3,1,5,3,2,1};
		int i=0;
		for(int j=1;j<arr.length;j++)
		{
			if(arr[j]!=arr[j-1])
			{
				arr[i++]=arr[j];
			}
		}
		System.out.println(arr[i]);
	}
}