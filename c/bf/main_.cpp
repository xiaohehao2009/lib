#include<cstdio>
#include<cmath>
#define CASE break;case
const int N=1<<20,M=1<<15;
char s[N],m[M];
struct E{
	int t,d;
} a[N];
int sta[N];
int main(int argc,char **argv){
	if(argc<2){
		printf("ARGUMENT LIST TOO SHORT: LENGTH %d\n",argc);
		return 1;
	}
	FILE *f=fopen(argv[1],"r");
	if(f==NULL){
		printf("NO SUCH FILE OR DIRECTORY: %s\n",argv[1]);
		return 1;
	}
	int len=fread(s,1,sizeof(s),f);
	if(len>=(int)sizeof(s)){
		printf("SOURCE TOO LARGE: REACH %d BYTES\n",len);
		return 1;
	}
	int tot=0,cnt=0;
	for(int i=0;i<len;i++){
		switch(s[i]){
		case '+':
			if(cnt&&(a[cnt-1].t==0||a[cnt-1].t==4))a[cnt-1].d++;
			else a[cnt++]={0,1};
		CASE '-':
			if(cnt&&(a[cnt-1].t==0||a[cnt-1].t==4))a[cnt-1].d--;
			else a[cnt++]={0,-1};
		CASE '>':
			if(cnt&&a[cnt-1].t==1)a[cnt-1].d++;
			else a[cnt++]={1,1};
		CASE '<':
			if(cnt&&a[cnt-1].t==1)a[cnt-1].d--;
			else a[cnt++]={1,-1};
		CASE '[':
			sta[tot++]=cnt;
			a[cnt++]={2,0};
		CASE ']':
			if(!tot){
				printf("NO MATCHING LEFT BRACKET: FOR CHAR AT %d\n",i+1);
				return 1;
			}
			if(cnt>1&&a[cnt-2].t==2&&a[cnt-1].t==0&&abs(a[cnt-1].d)==1){
				a[cnt-2]={4,0};
				cnt--;
				tot--;
			}
			else{
				a[sta[--tot]].d=cnt+1;
				a[cnt++]={3,sta[tot]+1};
			}
		CASE '.':
			a[cnt++]={5,0};
		CASE ',':
			a[cnt++]={6,0};
		}
	}
	if(tot){
		printf("NO MATCHING RIGHT BRACKET: FOR INSTRUCTION AT %d\n",sta[tot-1]+1);
		return 1;
	}
	int i=0,ptr=0;
	while(i<cnt){
		switch(a[i].t){
		case 0:
			m[ptr]+=a[i++].d;
		CASE 1:
			ptr+=a[i++].d;
#ifndef UNC
			if(ptr<0||ptr>=(int)sizeof(m)){
				printf("ACCESS OVER MEMORY: POINTER AT %d\n",ptr);
				return 1;
			}
#endif
		CASE 2:
			if(!m[ptr])i=a[i].d;
			else i++;
		CASE 3:
			if(m[ptr])i=a[i].d;
			else i++;
		CASE 4:
			m[ptr]=a[i++].d;
		CASE 5:
			fwrite(m+ptr,1,1,stdout);
			i++;
		CASE 6:
			fread(m+ptr,1,1,stdin);
			i++;
			break;
		default:
			__builtin_unreachable();
		}
	}
}