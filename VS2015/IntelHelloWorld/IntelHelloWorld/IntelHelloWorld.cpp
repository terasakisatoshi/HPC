// IntelHelloWorld.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <stdio.h>
#include <omp.h>
#include<iostream>
int main()
{
#pragma omp parallel
	{
		int ID = omp_get_thread_num();
		printf("Hello World thread num %d", ID);
	}
	system("pause");
    return 0;
}

