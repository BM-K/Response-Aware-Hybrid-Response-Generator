from lib import evaluation_utils
from multiprocessing import Pool

if __name__ == "__main__":

    path_to_save_test_ref = 'inference_results_ref_base_ko3_food.tsv'
    path_to_save_test_hyp = 'inference_results_hyp_base_ko3_food.tsv'
    path_to_ref_src_file = 'data/base_food_train.tsv'
    
    save_path = {'ref': path_to_save_test_ref, 'hyp': path_to_save_test_hyp, 'ref_src_file': path_to_ref_src_file}
    
    top1_out_file_path = save_path['hyp']
    hparams = {'test_tgt_file': path_to_save_test_ref, 'ref_src_file': save_path['ref_src_file']}

    metrics = 'bleu-1,bleu-2,bleu-3,bleu-4,distinct-1,distinct-2,entropy'.split(',')

    thread = 16
    thread_pool = Pool(thread)

    jobs = []
    scores = []
    for metric in metrics:
        if metric == 'entropy':
            job = thread_pool.apply_async(evaluation_utils.evaluate, (
                hparams['test_tgt_file'],
                top1_out_file_path,
                hparams['ref_src_file'],
                metric,
                3))
        else:
            job = thread_pool.apply_async(evaluation_utils.evaluate, (
                hparams['test_tgt_file'],
                top1_out_file_path,
                None,
                metric))
        jobs.append(job)
    
    print('\n=== Follow //transconsole/localization/machine_translation/metrics/bleu_calc.py ===')
    for job, metric in zip(jobs, metrics):
        complex_score = job.get()
        score = complex_score[0:len(complex_score) // 2]
        if len(score) == 1:
            score = score[0]

        print(('\n\t%s -> %s') % (metric, score))

        if type(score) is list or type(score) is tuple:
            for x in score:
                scores.append(str(x))
        else:
            scores.append(str(score))
