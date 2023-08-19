#include <stdio.h>
#include <string.h>

#define SWAP(x,y) if(x != y) {x ^= y; y ^= x; x ^= y;}

void perm(char* text, int l, int r){
	if(l == r)
		printf("%s\n", text);
	else for(int i = l; i <= r; i++){
		SWAP(text[i], text[l]);
		perm(text, l + 1, r);
		SWAP(text[i], text[l]);
	}
}

int main(){
	char buff[128];
	scanf("%s", buff);
	perm(buff, 0, strlen(buff) - 1);
}
