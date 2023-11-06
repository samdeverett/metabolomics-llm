# Glutamate

This is a proof of concept for developing a research assistant capable of synthesizing results from various papers.

In the PRISMA review ["Metabolite Concentration Changes in Humans After a Bout of Exercise: a Systematic Review of Exercise Metabolomics Studies"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7010904/), Figure 10 shows a mixed consensus on the effect of exercise on glutamate: several experiments show it increases while others show it decreases. We will test an LLM's ability to reproduce this analysis, with and without retrieval-augmented generation (RAG). Positive results would suggest RAG may successfully scale to reproducing these kinds of reviews. Negative results would suggest we should revisit the approach.

The papers from which the experimental results for [glutamate](https://en.wikipedia.org/wiki/Glutamate_(neurotransmitter)) (a.k.a. glutomic acid) are drawn can be found in Table S3 of [this file](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7010904/bin/40798_2020_238_MOESM1_ESM.docx). A summary of the results from each paper cited is below.

> [Breit, et al. (2015)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4552566/): Table 1 shows an **increase** in glutamate, specifically a 1.12 MFC and 0.17 log_2(MFC).  
> [Peake, et al. (2014)](https://journals.physiology.org/doi/full/10.1152/ajpendo.00276.2014?rfr_dat=cr_pub++0pubmed&url_ver=Z39.88-2003&rfr_id=ori%3Arid%3Acrossref.org): The plasma concentration of glutamate **increased** significantly only during high-intensity interval exercise. In skeletal muscle, glutamate consumption increases markedly during the first few minutes of exercise, particularly when muscle glycogen is low.  
> [Zauber, et al. (2012)](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/pmic.201100228): Table 2 shows an **increase** in glutamate in both males and females, although only significantly for females.  
> [Howe, et al. (2018)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5876003/): Table 1 shows a ratio of 0.528 for glutamate after an 80.5km run versus before, suggesting a **decrease** in glutamate.  
> [Coelho, et al. (2016)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5133105/): Glutamate was **up regulated** immediately following exercise but returned to origin levels shortly after.  
> [Danaher, et al. (2015)](https://link.springer.com/article/10.1007/s11306-015-0883-7): Glutamate significantly **decreased** during the recovery period after exercise.

Unfortunately, these results are ***not*** all stated in natural language within the texts. Here is how each is presented precisely.

> [Breit, et al. (2015)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4552566/): Referenced as "Glutamic_Acid" within a table.  
> [Peake, et al. (2014)](https://journals.physiology.org/doi/full/10.1152/ajpendo.00276.2014?rfr_dat=cr_pub++0pubmed&url_ver=Z39.88-2003&rfr_id=ori%3Arid%3Acrossref.org):
>> "Most amino acids did not change during HIIT or MOD, with the exception of the nonessential amino acids alanine (Fig. 5A), glutamate (Fig. 5B), and tyrosine (data not shown), which increased following HIIT (P < 0.05)."
>>  
>> "The plasma concentrations of alanine, glutamate, and tyrosine increased significantly only during high-intensity interval exercise."
>>
>> "In contrast with our findings, other studies have reported a decrease (40) or no change (59) in the concentration of glutamate in arterial plasma. In skeletal muscle, glutamate consumption increases markedly during the first few minutes of exercise, particularly when muscle glycogen is low (59). The consumption of glutamate in muscle may shift the alanine aminotransferase reaction in favor of the formation of alanine and TCA intermediates such as α-oxoglutarate (58). We can only speculate, but the increase in venous plasma glutamate concentration that we observed may have served to generate more TCA intermediates during high-intensity interval exercise."
>
> [Zauber, et al. (2012)](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/pmic.201100228): Referenced as "Glutamic acid (3TMS) within a table, and the response is denoted with a "↑" rather than words or numbers.  
> [Howe, et al. (2018)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5876003/): Referenced within a table, and the result is given as a ratio of post- to pre-exercise.  
> [Coelho, et al. (2016)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5133105/): "Glutamate was up regulated by 63% at T2, but regained the original levels at T4."  
> [Danaher, et al. (2015)](https://link.springer.com/article/10.1007/s11306-015-0883-7):
>> "During recovery, amino acid asparagine, saturated fatty acids dodecanoate, hexadecanoic acid methyl ester, hexadecanoate, and octadecanoic acid, saccharide gluconic acid, sugar alcohols xylitol, sugar xylose, TCA cycle intermediates citrate, glutamate, succinate, organophosphate glycerol-3-phosphate were significantly lower in the HIE300 % trial compared to the HIE150 % trial (p < 0.05), conversely uric acid, cholesterol and lactate were significantly higher in the HIE300 % trial compared to the HIE150 % at RC60 (p < 0.05)."
>> 
>> "Glutamate was significantly decreased during the recovery period following the HIE300 % trial only (p < 0.05)."

Given the fact that some results are presented in tables and as symbols (e.g., ↑) rather than words, we should expect a language model to struggle to correctly answer questions about the nuanced effects of exercise on glutamate. Doing so would require the model diverse capabilites, from parsing tabular data to understanding arrows and ratios to then synthesizing across documents.

To assess an LLM's ability, we will break these analyses of each compenent.

> **Experiment 1: Synthesis**  
> **Question:** Can the LLM combine insights from the various pieces of context given to it? Does it provide a balanced response if the pieces of context disagree?  
> **Methodology:** Generate a natural language summary of the result from each paper. With the summaries prepended to the prompt, ask the LLM about the effect of exercise on glutamate and assess it's ability to synthesize the summaries.

> **Experiment 2: Retrieval**  
> **Question:** Can the LLM retrieve the useful pieces of context needed to answer a question?
> **Methodology:** Embed the summaries from Experiment 1. Also embed other pieces of context that do not have to do with the effect of exercise on glutamate. Assess the model's ability to retrieve the summaries when asked about the effect of exercise on glutamate.

> **Experiment 3: RAG & Prompt Engineering**  
> **Question:** If the model retrieves the pieces of context it needs, does it use them properly?
> **Methodology:** Using the methodology from Experiment 2, ask the LLM about the effect of exercise on glutamate. Compare its response to the response from Experiment 1 where the summaries were prepended in the prompt. Experiment with RAG prompt templates until the output is desirable.

If all of these experiments are successful, we will then relax the assumption of having summaries of results and explore learning those summaries or being able to synthesize results directly from the documents (with tables, uncommon symbols, etc.) directly.
