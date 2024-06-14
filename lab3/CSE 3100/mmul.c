#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include "matrix.h"

// Search TODO to find the locations where code needs to be completed

#define     NUM_THREADS     2

typedef struct {
    unsigned int id;
    TMatrix *m, *n, *t;
} thread_arg_t;

static void * thread_main(void * p_arg)
{
    int i,j;
    thread_arg_t* dataval = (thread_arg_t*) p_arg;
    // TODO
    for (int i= dataval->id; i< dataval->m->nrows; i+=2)  
    {
        for (int j= 0; j< dataval->n->ncols;j++) 
        {
            TElement sum= (TElement) 0;
            for (int k= 0; k< dataval->m->ncols;k++)
            {
                sum+= dataval->m->data[i][k] * dataval->n->data[k][j];
            }
            dataval->t->data[i][j]= sum;
        }
           
    }
   
    return NULL;
}

/* Return the sum of two matrices.
 *
 * If any pthread function fails, report error and exit. 
 * Return NULL if anything else is wrong.
 *
 * Similar to mulMatrix, but with multi-threading.
 */
TMatrix * mulMatrix_thread(TMatrix *m, TMatrix *n)
{
    if (    m == NULL || n == NULL
         || m->ncols != n->nrows )
        return NULL;

    TMatrix * t = newMatrix(m->nrows, n->ncols);
    if (t == NULL)
        return t;

    // TODO
    pthread_t thread_1;
    pthread_t thread_2;

    thread_arg_t thread1;
    thread_arg_t thread2;

    thread1.n = n;
    thread1.id = 0;
    thread1.m = m;
    thread1.t  = t;

    pthread_create(&thread_1, NULL, thread_main,&thread1);

    thread2.id = 1; 
    thread2.n = n;
    thread2.t = t;
    thread2.m = m;

    pthread_create(&thread_2, NULL, thread_main,&thread2);

    pthread_join(thread_1, NULL); 
    pthread_join(thread_2, NULL); 

    return t;
}