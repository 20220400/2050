#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include "matrix.h"

#define     NUM_THREADS     2

typedef struct {
    unsigned int id;
    TMatrix *m, *n, *t;
} thread_arg_t;

/* the main function of threads */
static void * thread_main(void * p_arg)
{
    // TODO
    thread_arg_t* threaddata = (thread_arg_t*) p_arg;
    if(threaddata->id ==0){ for(int i = 0; i<((threaddata->m->nrows) / 2); i++)
        { for(int j = 0; j<threaddata->m->ncols; j++)
            { threaddata->t->data[i][j] = threaddata->m->data[i][j]+threaddata->n->data[i][j];
            }
        }}
    else{ for(int k = ((threaddata->m->nrows) / 2); k<threaddata->m->nrows; k++)
        { for(int l = 0; l<threaddata->m->ncols; l++)
            { threaddata->t->data[k][l] = threaddata->m->data[k][l]+threaddata->n->data[k][l];
            }
        }}
    pthread_exit(NULL);
    return NULL;
}

/* Return the sum of two matrices. The result is in a newly creaed matrix. 
 *
 * If a pthread function fails, report error and exit. 
 * Return NULL if something else is wrong.
 *
 * Similar to addMatrix, but this function uses 2 threads.
 */
TMatrix * addMatrix_thread(TMatrix *m, TMatrix *n)
{
    if (    m == NULL || n == NULL
         || m->nrows != n->nrows || m->ncols != n->ncols )
        return NULL;

    TMatrix * t = newMatrix(m->nrows, m->ncols);
    if (t == NULL)
        return t;

    // TODO

    pthread_t td_1;
    pthread_t td_2;
    thread_arg_t td1;
    thread_arg_t td2;

    td1.n = n;
    td1.id = 0; //parent thread here
    td1.m = m;
    td1.t  = t;

    pthread_create(&td_1, NULL, thread_main,&td1);

    td2.id = 1; //child thread here
    td2.n = n;
    td2.t = t;
    td2.m = m;

    pthread_create(&td_2, NULL, thread_main,&td2);

    pthread_join(td_1, NULL); //wait for parent ti findish
    pthread_join(td_2, NULL); //wait for child to finish

    return t;
}