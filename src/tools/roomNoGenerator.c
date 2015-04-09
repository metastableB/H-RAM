#include <stdio.h>

int main(int argc,char * argv[]) {
	int i=1;
	char c=*argv[1];
	for(i;i<=114;i++)
		printf("%c%03d\n",c,i);
}