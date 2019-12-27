//有一个天平,2克和7克砝码各一个。利用天平砝码在将140克盐分成50,90克两份。若规定只能使用3次天平进行称量，有哪些方法？
#include <iostream>
//#include "h1.h" 
#include <string>
using namespace std;

class chenyan{
private:
	//变量定义
	float start = 0, a1 = 0, a2 = 0, b1 = 0, b2 = 0, c1 = 0, c2 = 0;
	float aa2 = 0, bb2 = 0, cc2 = 0;//分量暂存器
	int n;   //记录第几步
	int i, j, k; //记录应该使用的方法
	int shu = 0;//记录可行的方法第几种
	float A1[10]; //用三个数组储存3步结果
	float A2[10];
	float A3[10];
public:
	//函数声明
	chenyan(float xx){ start = xx; };	//构造对象
	void func();        //功能实现
	float f(float x, int xx);	//具体方法实现
	void data(float x, float y, float y2, float nn, float eha2, float ehb2, float f, float  _f, float _a2, float _b2);
	void show(float x, float y, float y2, float nn, float eha2, float ehb2, float f, float  _f, float _a2, float _b2);
};

void chenyan::func(){
	for (i = 0; i < 13; i++){	//将盐start分为a1,a2
		n = 1;
		a1 = f(start, i);
		aa2 = a2;	//保存a2的原始值以便下层循环使用,因为a2在f()中会被不断改变

		for (j = 0; j < 30; j++){		//将盐a1分为b1,b2
			n = 2;
			a2 = aa2;//k循环结束，恢复变量值以便j循环使用
			b1 = f(a1, j);
			bb2 = b2;	//同上

			for (k = 0; k < 64; k++){			//将盐b1分为c1,c2
				n = 3;
				c1 = f(b1, k);

				if (c1 == 50 || c1 == 90){
					shu++;
					cout << "*****第【" << shu << "】种方法：*****" << endl;
					cout << start << " -> " << a1 << " -> " << b1 << " -> " << c1
						<< "  此时，i= " << i << "，j= " << j << "，k= " << k << endl;
					cout << "过程详解：" << endl;
					n = 1;	show(A1[0], A1[1], A1[2], A1[3], A1[4], A1[5], A1[6], A1[7], A1[8], A1[9]);
					n = 2;	show(A2[0], A2[1], A2[2], A2[3], A2[4], A2[5], A2[6], A2[7], A2[8], A2[9]);
					n = 3;	show(A3[0], A3[1], A3[2], A3[3], A3[4], A3[5], A3[6], A3[7], A3[8], A3[9]);
					cout << endl << endl;

				};

			}
		}
	}
}

void chenyan::data(float x, float y, float y2, float nn, float eha2, float ehb2, float f, float  _f, float _a2, float _b2){
	if (n == 1){
		A1[0] = x; A1[1] = y; A1[2] = y2; A1[3] = nn;  A1[4] = eha2; A1[5] = ehb2; A1[6] = f; A1[7] = _f; A1[8] = _a2; A1[9] = _b2;
	};
	if (n == 2){
		A2[0] = x; A2[1] = y; A2[2] = y2; A2[3] = nn;  A2[4] = eha2; A2[5] = ehb2; A2[6] = f; A2[7] = _f; A2[8] = _a2; A2[9] = _b2;
	};
	if (n == 3){
		A3[0] = x; A3[1] = y; A3[2] = y2; A3[3] = nn;  A3[4] = eha2; A3[5] = ehb2; A3[6] = f; A3[7] = _f; A3[8] = _a2; A3[9] = _b2;
	};
};

void chenyan::show(float x, float y, float y2, float nn, float eha2, float ehb2, float f, float  _f, float _a2, float _b2){
	cout << "第" << n << "步: " << endl;
	if (f > 0) { cout << "<将砝码" << f << "g放天平左侧>	"; };
	if (_f > 0){ cout << "<将砝码" << _f << "g放天平右侧>	"; };
	if (nn == 1){
		if (_a2 > 0){ cout << "<将分量【a2】:" << _a2 << "g放天平右侧>	"; };
		if (_b2 > 0){ cout << "<将分量【b2】:" << _b2 << "g放天平右侧>	"; };
		cout << endl << "从" << x << "g沙堆中取出" << y2 << "g沙子到天平左侧";
		if (n == 1){ cout << "(作为【a2】)，" << "剩下沙堆:" << x - y2 << "g(作为【a1】)"; };
		if (n == 2){ cout << "(作为【b2】)，" << "剩下沙堆:" << x - y2 << "g(作为【b1】)"; };
		if (n == 3){ cout << "(作为【c2】)，" << "剩下沙堆:" << x - y2 << "g(作为【c1】)"; };
		cout << endl;
	};
	if (nn == 2){
		cout << endl << "从" << x << "g沙堆中取出" << y - eha2 - ehb2 << "g沙子到天平左侧";
		if (n == 1){ cout << "(作为【a1】)，" << x - y + eha2 + ehb2 << "g到天平右侧(作为【a2】)"; };
		if (n == 2){ cout << "(作为【b1】)，" << x - y + eha2 + ehb2 << "g到天平右侧(作为【b2】)"; };
		if (n == 3){ cout << "(作为【c1】)，" << x - y + eha2 + ehb2 << "g到天平右侧(作为【c2】)"; };
		cout << endl;
	};

	if (eha2 > 0){
		cout << "将分量【a2】:" << eha2 << "g与所得沙堆合并得" << y;
		if (n == 2){ cout << "g (作新的【b1】)"; }
		else{ cout << "g (作新的【c1】)"; }
	}
	if (ehb2 > 0){ cout << "将分量【b2】:" << ehb2 << "g与所得沙堆合并得" << y << "g (作新的【c1】)"; };
	cout << endl;
}


float chenyan::f(float x, int fn){
	//jj = "【x平分为2份】"; jj = "【x加上砝码2g，平分为2份，取无砝码那份】";jj = "【x加上砝码2g，平分为2份，取有砝码那份】"; 
	float y, y2;//返回的结果
	switch (fn) {
	case 0:		y = x - 2; 	if (n == 1){ a2 = start - y; y2 = a2; };	if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 0, 2, 0, 0);		 break;
	case 1:		y = x - 5; 	if (n == 1){ a2 = start - y; y2 = a2; };	if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 2, 7, 0, 0);		 break;
	case 2:		y = x - 7; 	if (n == 1){ a2 = start - y; y2 = a2; };	if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 0, 7, 0, 0);		 break;
	case 3:		y = x - 9; 	if (n == 1){ a2 = start - y; y2 = a2; };	if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 0, 9, 0, 0);		 break;
	case 4:		y = (x + 0) / 2; 	if (n == 1){ a2 = start - y; y2 = a2; };	if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 2, 0, 0, 0, 0, 0, 0);		 break;
	case 5:		y = (x + 2) / 2; 	if (n == 1){ a2 = start - y; y2 = a2; };	if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 2, 0, 0, 0, 2, 0, 0);		 break;
	case 6:		y = (x + 2) / 2 - 2; 	if (n == 1){ a2 = start - y; y2 = a2; };	if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 2, 0, 0, 2, 0, 0, 0);		 break;
	case 7:		y = (x + 7) / 2; 	if (n == 1){ a2 = start - y; y2 = a2; };	if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 2, 0, 0, 0, 7, 0, 0);		 break;
	case 8:		y = (x + 7) / 2 - 7; 	if (n == 1){ a2 = start - y; y2 = a2; };	if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 2, 0, 0, 7, 0, 0, 0);		 break;
	case 9:		y = (x + 9) / 2; 	if (n == 1){ a2 = start - y; y2 = a2; };	if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 2, 0, 0, 0, 9, 0, 0);		 break;
	case 10:	y = (x + 9) / 2 - 2; 	if (n == 1){ a2 = start - y; y2 = a2; };	if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 2, 0, 0, 2, 7, 0, 0);		 break;
	case 11:	y = (x + 9) / 2 - 7; 	if (n == 1){ a2 = start - y; y2 = a2; };	if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 2, 0, 0, 7, 2, 0, 0);		 break;
	case 12:	y = (x + 9) / 2 - 9; 	if (n == 1){ a2 = start - y; y2 = a2; };	if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 2, 0, 0, 9, 0, 0, 0);		 break;
	case 13:	y = x - 2 - aa2; 		if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 0, 2, aa2, 0);		 break;
	case 14:	y = x - 5 - aa2; 		if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 2, 7, aa2, 0);		 break;
	case 15:	y = x - 7 - aa2; 		if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 0, 7, aa2, 0);		 break;
	case 16:	y = x - 9 - aa2; 		if (n == 2){ b2 = a1 - y;	y2 = b2; };	if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 0, 9, aa2, 0);		 break;
	case 17:	y = x - 2 + aa2; 		if (n == 2){ b2 = a1 - (y - a2);	y2 = b2; };	if (n == 3){ c2 = b1 - (y - a2);	y2 = c2; };	a2 = 0;	data(x, y, y2, 1, aa2, 0, 0, 2, 0, 0);		 break;
	case 18:	y = x - 5 + aa2; 		if (n == 2){ b2 = a1 - (y - a2);	y2 = b2; };	if (n == 3){ c2 = b1 - (y - a2);	y2 = c2; };	a2 = 0;	data(x, y, y2, 1, aa2, 0, 2, 7, 0, 0);		 break;
	case 19:	y = x - 7 + aa2; 		if (n == 2){ b2 = a1 - (y - a2);	y2 = b2; };	if (n == 3){ c2 = b1 - (y - a2);	y2 = c2; };	a2 = 0;	data(x, y, y2, 1, aa2, 0, 0, 7, 0, 0);		 break;
	case 20:	y = x - 9 + aa2; 		if (n == 2){ b2 = a1 - (y - a2);	y2 = b2; };	if (n == 3){ c2 = b1 - (y - a2);	y2 = c2; };	a2 = 0;	data(x, y, y2, 1, aa2, 0, 0, 9, 0, 0);		 break;
	case 21:	y = (x + 0) / 2 + aa2; 		if (n == 2){ b2 = a1 - (y - a2);	y2 = b2; };	if (n == 3){ c2 = b1 - (y - a2);	y2 = c2; };	a2 = 0;	data(x, y, y2, 2, aa2, 0, 0, 0, 0, 0);		 break;
	case 22:	y = (x + 2) / 2 + aa2; 		if (n == 2){ b2 = a1 - (y - a2);	y2 = b2; };	if (n == 3){ c2 = b1 - (y - a2);	y2 = c2; };	a2 = 0;	data(x, y, y2, 2, aa2, 0, 0, 2, 0, 0);		 break;
	case 23:	y = (x + 2) / 2 - 2 + aa2; 		if (n == 2){ b2 = a1 - (y - a2);	y2 = b2; };	if (n == 3){ c2 = b1 - (y - a2);	y2 = c2; };	a2 = 0;	data(x, y, y2, 2, aa2, 0, 2, 0, 0, 0);		 break;
	case 24:	y = (x + 7) / 2 + aa2; 		if (n == 2){ b2 = a1 - (y - a2);	y2 = b2; };	if (n == 3){ c2 = b1 - (y - a2);	y2 = c2; };	a2 = 0;	data(x, y, y2, 2, aa2, 0, 0, 7, 0, 0);		 break;
	case 25:	y = (x + 7) / 2 - 7 + aa2; 		if (n == 2){ b2 = a1 - (y - a2);	y2 = b2; };	if (n == 3){ c2 = b1 - (y - a2);	y2 = c2; };	a2 = 0;	data(x, y, y2, 2, aa2, 0, 7, 0, 0, 0);		 break;
	case 26:	y = (x + 9) / 2 + aa2; 		if (n == 2){ b2 = a1 - (y - a2);	y2 = b2; };	if (n == 3){ c2 = b1 - (y - a2);	y2 = c2; };	a2 = 0;	data(x, y, y2, 2, aa2, 0, 0, 9, 0, 0);		 break;
	case 27:	y = (x + 9) / 2 - 2 + aa2; 		if (n == 2){ b2 = a1 - (y - a2);	y2 = b2; };	if (n == 3){ c2 = b1 - (y - a2);	y2 = c2; };	a2 = 0;	data(x, y, y2, 2, aa2, 0, 2, 7, 0, 0);		 break;
	case 28:	y = (x + 9) / 2 - 7 + aa2; 		if (n == 2){ b2 = a1 - (y - a2);	y2 = b2; };	if (n == 3){ c2 = b1 - (y - a2);	y2 = c2; };	a2 = 0;	data(x, y, y2, 2, aa2, 0, 7, 2, 0, 0);		 break;
	case 29:	y = (x + 9) / 2 - 9 + aa2; 		if (n == 2){ b2 = a1 - (y - a2);	y2 = b2; };	if (n == 3){ c2 = b1 - (y - a2);	y2 = c2; };	a2 = 0;	data(x, y, y2, 2, aa2, 0, 9, 0, 0, 0);		 break;
	case 30:	y = x - 2 - bb2; 					if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 0, 2, 0, bb2);		 break;
	case 31:	y = x - 5 - bb2; 					if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 2, 7, 0, bb2);		 break;
	case 32:	y = x - 7 - bb2; 					if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 0, 7, 0, bb2);		 break;
	case 33:	y = x - 9 - bb2; 					if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 0, 9, 0, bb2);		 break;
	case 34:	y = x - 2 + bb2;					if (n == 3){ c2 = b1 - (y - b2);	y2 = c2; };		data(x, y, y2, 1, 0, bb2, 0, 2, 0, 0);		 break;
	case 35:	y = x - 5 + bb2;					if (n == 3){ c2 = b1 - (y - b2);	y2 = c2; };		data(x, y, y2, 1, 0, bb2, 2, 7, 0, 0);		 break;
	case 36:	y = x - 7 + bb2;					if (n == 3){ c2 = b1 - (y - b2);	y2 = c2; };		data(x, y, y2, 1, 0, bb2, 0, 7, 0, 0);		 break;
	case 37:	y = x - 9 + bb2;					if (n == 3){ c2 = b1 - (y - b2);	y2 = c2; };		data(x, y, y2, 1, 0, bb2, 0, 9, 0, 0);		 break;
	case 38:	y = (x + 0) / 2 + bb2;					if (n == 3){ c2 = b1 - (y - b2);	y2 = c2; };		data(x, y, y2, 2, 0, bb2, 0, 0, 0, 0);		 break;
	case 39:	y = (x + 2) / 2 + bb2;					if (n == 3){ c2 = b1 - (y - b2);	y2 = c2; };		data(x, y, y2, 2, 0, bb2, 0, 2, 0, 0);		 break;
	case 40:	y = (x + 2) / 2 - 2 + bb2;					if (n == 3){ c2 = b1 - (y - b2);	y2 = c2; };		data(x, y, y2, 2, 0, bb2, 2, 0, 0, 0);		 break;
	case 41:	y = (x + 7) / 2 + bb2;					if (n == 3){ c2 = b1 - (y - b2);	y2 = c2; };		data(x, y, y2, 2, 0, bb2, 0, 7, 0, 0);		 break;
	case 42:	y = (x + 7) / 2 - 7 + bb2;					if (n == 3){ c2 = b1 - (y - b2);	y2 = c2; };		data(x, y, y2, 2, 0, bb2, 7, 0, 0, 0);		 break;
	case 43:	y = (x + 9) / 2 + bb2;					if (n == 3){ c2 = b1 - (y - b2);	y2 = c2; };		data(x, y, y2, 2, 0, bb2, 0, 9, 0, 0);		 break;
	case 44:	y = (x + 9) / 2 - 2 + bb2;					if (n == 3){ c2 = b1 - (y - b2);	y2 = c2; };		data(x, y, y2, 2, 0, bb2, 2, 7, 0, 0);		 break;
	case 45:	y = (x + 9) / 2 - 7 + bb2;					if (n == 3){ c2 = b1 - (y - b2);	y2 = c2; };		data(x, y, y2, 2, 0, bb2, 7, 2, 0, 0);		 break;
	case 46:	y = (x + 9) / 2 - 9 + bb2;					if (n == 3){ c2 = b1 - (y - b2);	y2 = c2; };		data(x, y, y2, 2, 0, bb2, 9, 0, 0, 0);		 break;
	case 47:	if (a2>0){ y = x - 2 - aa2 - bb2; 					if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 0, 2, aa2, bb2); }
				else{ y = NULL; };	 break;
	case 48:	if (a2>0){ y = x - 5 - aa2 - bb2; 					if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 2, 7, aa2, bb2); }
				else{ y = NULL; };	 break;
	case 49:	if (a2>0){ y = x - 7 - aa2 - bb2; 					if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 0, 7, aa2, bb2); }
				else{ y = NULL; };	 break;
	case 50:	if (a2>0){ y = x - 9 - aa2 - bb2; 					if (n == 3){ c2 = b1 - y;	y2 = c2; };		data(x, y, y2, 1, 0, 0, 0, 9, aa2, bb2); }
				else{ y = NULL; };	 break;
	case 51:	if (a2>0){ y = x - 2 + aa2 + bb2;  					if (n == 3){ c2 = b1 - (y - a2 - b2);	y2 = c2; };		data(x, y, y2, 1, aa2, bb2, 0, 2, 0, 0); }
				else{ y = NULL; };	 break;
	case 52:	if (a2>0){ y = x - 5 + aa2 + bb2;  					if (n == 3){ c2 = b1 - (y - a2 - b2);	y2 = c2; };		data(x, y, y2, 1, aa2, bb2, 2, 7, 0, 0); }
				else{ y = NULL; };	 break;
	case 53:	if (a2>0){ y = x - 7 + aa2 + bb2;  					if (n == 3){ c2 = b1 - (y - a2 - b2);	y2 = c2; };		data(x, y, y2, 1, aa2, bb2, 0, 7, 0, 0); }
				else{ y = NULL; };	 break;
	case 54:	if (a2>0){ y = x - 9 + aa2 + bb2;  					if (n == 3){ c2 = b1 - (y - a2 - b2);	y2 = c2; };		data(x, y, y2, 1, aa2, bb2, 0, 9, 0, 0); }
				else{ y = NULL; };	 break;
	case 55:	if (a2>0){ y = (x + 0) / 2 + aa2 + bb2;  					if (n == 3){ c2 = b1 - (y - a2 - b2);	y2 = c2; };		data(x, y, y2, 2, aa2, bb2, 0, 0, 0, 0); }
				else{ y = NULL; };	 break;
	case 56:	if (a2>0){ y = (x + 2) / 2 + aa2 + bb2;  					if (n == 3){ c2 = b1 - (y - a2 - b2);	y2 = c2; };		data(x, y, y2, 2, aa2, bb2, 0, 2, 0, 0); }
				else{ y = NULL; };	 break;
	case 57:	if (a2>0){ y = (x + 2) / 2 - 2 + aa2 + bb2;  					if (n == 3){ c2 = b1 - (y - a2 - b2);	y2 = c2; };		data(x, y, y2, 2, aa2, bb2, 2, 0, 0, 0); }
				else{ y = NULL; };	 break;
	case 58:	if (a2>0){ y = (x + 7) / 2 + aa2 + bb2;  					if (n == 3){ c2 = b1 - (y - a2 - b2);	y2 = c2; };		data(x, y, y2, 2, aa2, bb2, 0, 7, 0, 0); }
				else{ y = NULL; };	 break;
	case 59:	if (a2>0){ y = (x + 7) / 2 - 7 + aa2 + bb2;  					if (n == 3){ c2 = b1 - (y - a2 - b2);	y2 = c2; };		data(x, y, y2, 2, aa2, bb2, 7, 0, 0, 0); }
				else{ y = NULL; };	 break;
	case 60:	if (a2>0){ y = (x + 9) / 2 + aa2 + bb2;  					if (n == 3){ c2 = b1 - (y - a2 - b2);	y2 = c2; };		data(x, y, y2, 2, aa2, bb2, 0, 9, 0, 0); }
				else{ y = NULL; };	 break;
	case 61:	if (a2>0){ y = (x + 9) / 2 - 2 + aa2 + bb2;  					if (n == 3){ c2 = b1 - (y - a2 - b2);	y2 = c2; };		data(x, y, y2, 2, aa2, bb2, 2, 7, 0, 0); }
				else{ y = NULL; };	 break;
	case 62:	if (a2>0){ y = (x + 9) / 2 - 7 + aa2 + bb2;  					if (n == 3){ c2 = b1 - (y - a2 - b2);	y2 = c2; };		data(x, y, y2, 2, aa2, bb2, 7, 2, 0, 0); }
				else{ y = NULL; };	 break;
	case 63:	if (a2>0){ y = (x + 9) / 2 - 9 + aa2 + bb2;  					if (n == 3){ c2 = b1 - (y - a2 - b2);	y2 = c2; };		data(x, y, y2, 2, aa2, bb2, 9, 0, 0, 0); }
				else{ y = NULL; };	 break;
	};

	return y;
}



int main(){
	cout << "有一个天平,2克和7克砝码各一个。利用天平砝码在将140克盐分成50,90克两份。若规定只能使用3次天平进行称量，有哪些方法？" << endl;
	chenyan f1(140);
	f1.func();
	return 0;
}
