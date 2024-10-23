import streamlit as st
from streamlit_option_menu import option_menu

# Page configuration
st.set_page_config(page_title="CJD", layout= 'wide')

# Adding coloured gradients for formatting
st.markdown('''
<style> [data-testid="stAppViewContainer"]{background-color:hsla(240,70%,8%,1);
background-image:
radial-gradient(at 40% 20%, hsla(0,95%,49%,0.47) 0px, transparent 50%),
radial-gradient(at 80% 0%, hsla(189,100%,56%,1) 0px, transparent 50%),
radial-gradient(at 0% 0%, hsla(336,62%,68%,1) 0px, transparent 50%);}</style>
''', unsafe_allow_html= True)

st.markdown('''
<style> [data-testid="stHeader"]{background-color:hsla(240,92%,5%,1);
}</style>
''', unsafe_allow_html= True)
# Page title header and subheader
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');

    .title-font {
        font-family: 'Libre Baskerville', serif;
        font-size: 48px;
        font-weight: bold;
        color: #FFF;
    }
    .SubHeading-font{
        font-family: 'Libre Baskerville', serif;
        font-size: 18px;
        font-weight: 400;
        color: #FFF;
    }
    .Header-font{
        font-family: 'Libre Baskerville', serif;
        font-size: 37px;
        font-weight: bold;
        color: #FFF;
    }
    </style>
    """, unsafe_allow_html=True)
with st.container():
    l1,r1 = st.columns(2)
    with l1:
        #st.title("Understanding Creutzfeldt-Jakob Disease")
        st.markdown('<p class="title-font">Understanding Creutzfeldt-Jakob Disease</p>', unsafe_allow_html=True)
        st.write("#####")
        st.caption("*_:blue[Why] and :blue[how] does it affects the :blue[humans]?_*")
    with r1:
        l2,r2,m2 = st.columns(3)
        with m2:
            #st.write("#####")
            st.image("m2H7i8b1K9K9K9Z5.png", width = 150)
    
# Creating nav menu
#["Overview", "Cases", "Causes", "Complications", "Treatment", "Awareness", "Related content", "Sources"]



selected = option_menu(
    menu_title=None,
    options=["Overview & Causes", "Case Analysis", "Complications & Treatment", "Related content & Sources"],
    icons=['book-half', 'graph-up-arrow', 'prescription', 'info-circle'],
    orientation="horizontal",
    styles={
        'container': {
            "padding": "0",
            "background-color": "transparent"
        },
        'nav-link': {
            'font-size': '12px',
            'padding': '10px',
            'color': 'white',
        },
        'nav-link-selected': {
            'background-color': 'hsla(240,92%,5%,1)'
        }
    }
)
st.write("---")

#### OVERVIEW ####

if selected == "Overview & Causes":
    #st.title("What is CJD actually?")
    st.markdown('<h4 class="Header-font">What is CJD actually?</h4>', unsafe_allow_html=True)
    st.caption("*Brief look towards CJD; Prion diseases in general!*")
    with st.container():
        l,r  = st.columns(2)
        with l:
            st.write("<h3 class='SubHeading-font'> <i><b>Understanding the variations</b></i></h3>", unsafe_allow_html=True)
            st.write("Creutzfeldt-Jakob disease (CJD) is a rapidly progressive, rare, transmissible, and universally fatal neurodegenerative condition caused by prion proteins. The condition has a long incubation period. **[3][4]** CJD was first described in 1920 by Hans Creutzfeldt and later in 1921 and 1923 by Alfons Jakob. Later, Clearance J. Gibbs started using the term Creutzfeldt-Jacob disease because the acronym CJD was closer to his initials.**[5][6]**")
            st.write("CJD primarily affects the central nervous system (CNS). The CNS' chief functional unit is the neuron, a unique cell type that can receive, store, and transmit information. CNS neurons do not regenerate, although some regions of the brain can heal to a limited extent due to the presence of stem cells.**[2]**")
            st.write("Neurons in the brain are topographically organized, with functional domains existing in anatomically defined regions. For example, the cerebral cortex controls voluntary movements, while the hypothalamus plays a huge role in autonomic responses. The brain cells' somatotopic organization allows various body areas to receive sensory and motor input from the CNS, which is valuable in localizing neurologic lesions. CJD neuronal inclusions damage brain neurons, manifesting with nonspecific prodromal symptoms early in the disease course and neurologic changes, particularly myoclonus, in the advanced stages.**[2]**")
            st.write("Creutzfeldt-Jakob disease (CJD) is a rare, fatal degenerative brain disorder caused by prion proteins. This condition belongs to a group of transmissible spongiform encephalopathies affecting people worldwide, with an incidence of 1 case per million per year. Approximately 350 cases are diagnosed annually in the United States. Death occurs in nearly 70 percent of patients within a year. Prompt and accurate diagnosis of CJD impacts intervention strategies and overall outcomes.")
            st.write("CJD belongs to family of human and animal diseases known as Transmissible Spongiform Encephalopathies (TSEs). Simply known as Prion disease. ***Human prion diseases*** include CJD and vCJD, Gertsmann-Straussler-Schenkar Disease, Fatal familial insomnia, Kuru. ***Animal prion diseases*** include BSE or mad cow disease, Mink encephalopathy, Feline encephalopathy, Scrapie,  Chronic Wasting Disease.")
            st.write("**Sporadic CJD**")
            st.write("In the early stages of sporadic CJD, patients may develop nonspecific symptoms like vertigo, headache, fatigue, and sleep disorders. However, memory problems, agitation, irritability, depression, apathy, mood swings, and sensory changes like vision loss can also occur. As the disease advances, patients may develop rapidly worsening confusion, disorientation, and cognitive problems. Most patients manifest with coordination and movement abnormalities, including ataxia, involuntary jerky movements, myoclonus, muscle stiffness, and involuntary muscle twitching. Myoclonus persists during sleep and may be elicited by loud sounds or bright lights. Extrapyramidal symptoms like bradykinesia, dystonia, and rigidity may occur. Patients gradually lose mobility and speech and progress into a comatose state. Certain infections, such as pneumonia, can lead to death. Patients with sporadic CJD are typically between 55 and 75 years old. Death occurs within a year of onset, with the median duration of illness being 4 to 5 months. The median age of death in individuals with sporadic CJD is 68 years. Sporadic CJD is similar to dementia in presentation but progresses much more rapidly. CJD subtyping is based on genetic polymorphism, prion protein characteristics, and associated symptoms. ")
            st.write("Methionine/methionine type 1 (MM1) and methionine/valine type 1 (MV1) comprise 70 percent of cases and correlate with the classic CJD phenotype. The condition has a mid- to late-life onset and presents with rapidly progressive dementia (RPD) and early myoclonus and ataxia. Methionine/valine type 2 (MV2) is the kuru plaque variant, comprising 10 percent of sporadic CJD cases. The condition presents with progressive dementia with prominent psychiatric features and has a longer duration (about 17 months).The valine/valine type 2 (VV2) variant is also known as the ataxic variant. The condition presents with ataxia at the onset or as an isolated feature. The VV2 subtype has a duration of illness of about 7 to 9 months. The methionine/methionine type 2 (MM2) subtype may be classified as either thalamic or cortical. The thalamic MM2 subtype is also known as sporadic fatal insomnia and is present in 2 percent of cases. The mean disease duration is 15.6 months. The most frequent symptoms include psychomotor hyperactivity, ataxia, insomnia, and cognitive impairment, resembling fatal familial insomnia. The cortical MM2 subtype also comprises 2% of sporadic CJD cases. Dementia is the predominant manifestation of this condition. The average disease duration is 15.7 months. Visual and cerebellar signs are rarely described at presentation. The valine/valine 1 (VV1) subtype comprises 1 percent off cases and has a younger age of onset. Individuals with this condition present with progressive dementia. The VV1 subtype has an average duration of 15.3 months.**[2]**")
            st.write("**Inherited CJD**")
            st.write("Genetic CJD has phenotypic variability that may be attributed to the low penetrance of PRNP mutations. Patients with genetic CJD are usually younger than individuals with sporadic CJD, manifesting behavioral and cognitive changes initially, and incoordination and movement abnormalities over the next few months. A family history of similar neurologic manifestations may be elicited. Inherited CJD is fatal, though the duration of illness varies individually. For example, Gerstmann–Straussler–Scheinker syndrome has a slow progression, and death may be delayed for up to 10 years.**[10]**")
            st.write("**Variant CJD**")
            st.write("Patients with variant CJD are often younger than patients with sporadic CJD, initially presenting with psychiatric symptoms, behavioral changes, and painful dysesthesias. Movement disorders may develop early, but dementia is usually a late sign. A history of a neurosurgical procedure or ingestion of infected meat may be elicited. The median duration of illness is between 13 and 14 months, while the median age at death is 28 years.**[2]**")
            st.write("###")
            st.write("<h3 class='SubHeading-font'> <i><b>Etiology</b></i></h3>", unsafe_allow_html=True)
            st.write('The normal, harmless prion protein is usually designated as PrPC (C stands for cellular) and the abnormal, infectious form (which causes the disease) is PrPSc (Sc stands for prototypical prion disease scrapie).The normal, harmless prion protein is usually designated as PrPC (C stands for cellular) and the abnormal, infectious form (which causes the disease) is PrPSc (Sc stands for prototypical prion disease scrapie).The normal, harmless prion protein is usually designated as PrPC (C stands for cellular) and the abnormal, infectious form (which causes the disease) is PrPSc (Sc stands for prototypical prion disease scrapie). In the acquired form of the disease, the infectious PrPSc comes from the outside the body, for example, through contaminated meat as is seen in variant CJD.  In the hereditary form, infectious prions can arise when a mutation occurs in the gene for the bodys normal prion protein. As the mutated PrPC duplicates itself, it spontaneously changes shape into the infectious form. (Prions themselves do not contain genetic information and do not require genes to reproduce themselves.)  If the prion protein gene is changed in a persons sperm or egg cells, the changed gene can be transmitted to the persons children. Specific changes found in each family affects how often the disease appears and what symptoms are most noticeable. However, not all people with mutations in the prion protein gene develop CJD. In the sporadic form, the infectious prions are believed to be made by an error in the cells machinery that makes proteins and controls their quality. These errors are more likely to occur with aging.')
            st.write("###")
            st.write("<h3 class='SubHeading-font'> <i><b>Epidemiology</b></i></h3>", unsafe_allow_html=True)
            st.write("CJD affects about 1 individual per million per year worldwide. Approximately 350 cases are diagnosed annually in the United States. Sporadic CJD is the most common form of human prion disease. The condition has a mean onset age of 62, although it has also been reported in younger and older age groups.**[7][8]** Sporadic CJD has a 1:1 male-to-female ratio. Approximately 1 to 2 new sporadic CJD cases appear per 1,000,000 individuals worldwide annually.**[9]** Death occurs in nearly 70% of patients within a year of onset. The mean survival of sporadic CJD is 4 to 8 months, with 90 percent of patients dying within a year. **[2]**")
            st.write("Genetic CJD is the second most common type of this condition. Patients often have a family history and autosomal-dominant PRNP gene mutations. Acquired cases are seen in less than 1 percent of cases, usually in young adults with a mean age of 29.")
        with r:
            r1,r2,r3 = st.columns(3)
            with r2:
                st.image("Pathophysiology.png", width=500, caption="Elucidating Critical Proteinopathic Mechanisms and Potential Drug Targets in Neurodegeneration - Scientific Figure on ResearchGate. Available from: https://www.researchgate.net/figure/Pathophysiology-of-Creutzfeldt-Jakob-disease-CJD-Factors-like-mutations-in-prion-gene_fig3_336264113 [accessed 22 Oct 2024]")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
            r1,r2,r3 = st.columns(3)
            with r2:
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                
                st.image("Pathogenesis.png", width=550)
                
    st.write("###")
    #st.title("Why and how it occurs?")
    st.markdown('<h4 class="Header-font">The question of "why?" and "how?"</h4>', unsafe_allow_html=True)
    st.caption("*A summerised description for the causes of :blue[CJD]*")
    with st.container():
        l1, r1 = st.columns(2)
        with l1:
            st.write('mostly occuring in later stages of life, mainly in 60s, it is not a transmissible disease. A person cannot get CJD through air or touchimg somone or something like a doorknob. or being close to someone who has CJD. There is a very small risk that a surgeon or others who handle brain tissue following a brain biopsy or autopsy may become accidentally infected. Special surgical and disinfection procedures can markedly reduce this risk. There is no evidence that caregivers, healthcare workers, and those who prepare bodies for funerals and cremation have an increased risk of prion disease when compared to the general population. Still, clinical advice prohibits the infected individual from donating blood, organs and tissues.')
            st.write("Why? you may ask, the reasonis prions. Prions are abnormal proteins which undergo abnormal folding which subjects them to an unusual conformation which specifically targets the other proteins, in turn converting them into prions. Proteins are long chains of amino acids that fold together into a unique shape or conformation to help a cell function in a particular way. The normal and harmless prion protein is found throughout the body but is most abundant in the nervous system. Its overall role is not fully understood. This abnormal folding or conformation is “transmitted” to normal prion proteins in surrounding nerve cells, causing them to become infective and changed to one that results in the disease. Once they are formed, abnormal prion proteins aggregate, or clump together, which may lead to the nerve cell loss and other brain damage seen in CJD.**[1]**")

####CASES#####

if selected == "Case Analysis":
    #st.title("Connecting the dots: Case analysis")
    st.markdown('<h4 class="Header-font">Connecting the dots: Case analysis</h4>', unsafe_allow_html=True)
    st.caption("*Understanding the occurance and history of the :blue[CJD]*")
    st.write("<h3 class='SubHeading-font'> <i><b>First Occurence</b></i></h3>", unsafe_allow_html= True)
    st.write("In May 1995,  19 year-old Steven Churchill of Wilshire England, a previously healthy young man began exhibiting signs of dementia his symptoms included poor memory loss of motor functions and the onset of severe depression. He transitioned from a healthy young man to a confused wheelchair bound Nursing Home Patient in a matter of weeks. Sadly just 6 months after the appearance of his symptoms he succumbed to the effects of aggressive neurological degeneration. Churchill was one of many victims of a new Variant of **Bovine Spongiform Encephalopathy (BSE)** also known as **mad cow disease** causes the degeneration of neurons in the brains of cattle and more recently humans. In the mid 1990s, the UK experienced a significant outbreak of bovine spongiform encephalopathy  this triggered widespread hysteria concerns about the meat industry and a Severe loss of trust in the UK government due to its inadequate and delayed response.")
    with st.container():
        l1,m1,r1 = st.columns(3)
        with m1:
            st.image("Memorial_plaque_to_victims_of_vCJD.jpg", caption = "A plaque memorializing those who died of vCJD.", width = None)
    st.write("<h3 class='SubHeading-font'> <i><b>Havoc in England</b></i></h3>", unsafe_allow_html= True)
    st.write("Human prions are only transferred through cannibalism. This is a good reason why it's looked down upon to eat people. This is also how mad cow disease was initially spread. Cows that were predisposed and prions were slaughtered. Some of the infected meat was added to cow feed known as MGM or meat and bone meal MGM cow feed was given to cattle and was a common practice in the industry at the time cows fed with contaminated feed ingested cattle meat containing prions leading to infection. Subsequently infected cows were processed for meat and some was added to cow feed once again. This cyclic process perpetuated the spread of prions eventually tainted meat reached supermarkets where it was spread to Consumers. Failure to enforce crucial measures led to the most significant food contamination outbreak in UK history ultimately culminating in the notorious mad cow disease outbreak. **The origins of the outbreak can be traced to a cattle farm in Sussex, England**. In December 1984, cattle began showing symptoms suggestive of BSE. Postmortem examinations conclusively diagnose the animals with BSE. It was discovered that the cows had been consuming feed containing meat and bone meal or MBM derived from cattle affected by BSE. Unfortunately very minimal precautions were implemented to curtail the spread of BSE within the cattle population or invest at implications for human consumption. In 1989, as cases of BSE infections continued to escalate among cattle, the UK government took decisive action by prohibiting the sale of cattle organ Meats including brain and spinal cord, however they continued the sale of General cattle meat to the public. Simultaneously,  the US imposed bans on imports of live cattle, sheep, bison and goats from Nations where BSE had been identified. Agriculture Minister John Gummer assured the public of the safety of beef consumption. On May 16th 1990, Gummer delivered a now Infamous broadcast aimed at demonstrating the safety of beef consumption by having his four-year-old daughter Cordelia take a bite from a hamburger. When Gummer offered her a bite she refused on National Television perhaps serving as an ominous indication of the events to come, During the peak of the outbreak between 1992 and 1993,  more than 180,000 cattle tested positive for BSE marking the peak number of infections, Despite the surge, the UK government maintained its position offering reassurances to the public that humans were no more than dead and hosts.")
    st.write("On May 21st 1995, 19-year-old Steven Churchill became the first victim of this new disease subsequently labeled **variant Creutzfeldt-Jakob Disease** or **vCJD**. Despite mounting concerns, the UK government persisted in asserting the safety of British beef and maintained that there was insufficient evidence to establish a definitive link between BSE and the new variant found in Churchill. A second case of variant Creutzfeldt-Jakob Disease affected a 25-year-old male named Peter Hall and would sadly meet he same fate as Churchill. Not long after Steven Doro, the Secretary of State for health disclosed a pivotal finding variant Creutzfeldt-Jakob Disease was linked to the consumption of cattle meat contaminated with prions responsible for BSE. Public outrage Rose to anger compelling the UK to take decisive action by Banning the use of MBM feed for livestock testing and tracking for cattle soon followed this triggered a dramatic decline in beef consumption across the UK. Europe, the US and Canada imposed a ban on All Imports of UK meat. The UK government itself implemented a sweeping prohibition on all beef sales for a period of 30 months in March 1996. A robust campaign was initiated to confront the escalating threat of BC among cattle the campaign called for over 4.5 million cattle to be systematically slaughtered to isolate the transmission of BSE in 1999. Following quarantine measures and extensive testing the incidence of BSE finally began to decline with levels reaching a manageable point,  the UK government lifted the ban on all meat products .The toll on the UK cattle industry was staggering amounting to a colossal $2.4 billion in losses tragically 178 lives were lost to variant Creutzfeldt-Jakob Disease as a result of consuming contaminated beef the low infection rates among humans were attributed to several key factors these included intense public pressure and media scrutiny of the UK government's reluctance to investigate transmission to humans. The public's confidence in the government was severely affected, while the government did not intentionally deceive the public its strategy of offering reassurances proved to be a misstep. Moreover scientific advisory committees were criticized for their slow decisions. The UK mad cow disease outbreak became a classic lesson in epidemiology underscoring The Perils of failing to discern clear disease patterns and hesitating to conduct investigations It showed how failing to take simple precautions resulted in widespread catastrophe.")
    with st.container():
        l2,m2,r2 = st.columns(3)
        with m2:
            st.image("ESB_UK-1987-2008.svg.png", caption = "Deaths in the UK caused by vCJD from the start of the BSE outbreak up until 2009. MM and MV refer to the two genotypes of vCJD.", width = None)
    st.write("###")
    st.write("<h3 class='SubHeading-font'> <i><b>Kuru: an unsettling outbreak in Papua New Guinea</b></i></h3>", unsafe_allow_html= True)
    st.write("**Kuru**, a fascinating and Elusive malady that continues to Peak the Curiosity of medical Minds across the globe an intriguing puzzle of medical history. Kuru was first discovered in the mid 20th century. It was among the indigenous four people of Papua New Guinea that this mysterious illness made its initial appearance astounding the world with its Rarity and unique characteristics. Unlike most diseases isn't caused by bacteria or viruses then what causes it well it's the work of prions, tiny misfolded proteins that wreak havoc on our bodies. Let's travel back in time to the four people of Papua New Guinea, their cultural practice of cannibalism specifically consuming the brains of their deceased unwittingly opened the door to these mischievous prions. A person died of Kuru their brain was chock full of these prions, by consuming the brain, the four people were directly ingesting these prions, setting the stage for their own bodies to fall victim to Kuru. These silent yet formidable adversaries are the culprits behind Kuru called causing a disease that baffles the world. Kuru presents itself initially with a Triad of unusual symptoms the first symptom is Tremors a rhythmic shaking that often starts in the hands and can spread throughout the body. The second symptom is an unsteady gate the medical term for a change in how a person walks. A patient with Kuru may appear to stagger or stumble their balance compromised by the diseases. Insidious attack on their nervous system. The third symptom emotional instability can manifest in a myriad of ways some patients display inappropriate laughter, while others may swing between moods without warning. As the disease progresses, these symptoms worsen. The tremors become more pronounced. It's a gradual but Relentless assault on the nervous system leading to severe neurological damage, eventually the patient may become unable to move or speak this stage is often followed by a period of unresponsiveness before the disease claims its final Victory.")
    with st.container(border=True):
            
            st.markdown("<h4 class='SubHeading-font'><i>Gallery</i></h4>", unsafe_allow_html=True)
            
            l3,m3,r3 = st.columns(3)
            
            with m3:
                st.write("###")
                st.image("Fore_child_in_advanced_kuru_stage.png", caption = "A Fore child with advanced kuru. He is unable to walk or sit upright without assistance and is severely malnourished.", width = 500)
            with l3:
                st.write("###")
                st.image("korowai-with-skull.jpeg", caption = "Korowai Tribe: The Remote Papuan People Who May Be Cannibals", width = 500)
            with r3:
                st.write("###")
                st.image("AS219611.jpg", caption= "Cannibal tribe ate humans 'whole' except for one 'bitter' part.")


#### COMPLICATIONS ####

if selected == "Complications & Treatment":
    #st.title("Symptoms, Diagnosis and Remedies")
    st.markdown('<h4 class="Header-font">Symptoms, Diagnosis and Remedies</h4>', unsafe_allow_html=True)
    st.caption("*Is there any way to reticulate :blue[CJD]?*")
    with st.container():
        l,r = st.columns(2)
        with l:
            st.write("<h3 class='SubHeading-font'> <i><b> Symptoms: Early and late</b></i></h3>", unsafe_allow_html=True)
            st.write("CJD is rare, worsens rapidly while changing the brain tissue composition, cognitive degradation as well as muscle functions. Two chief symptoms are mental deterioration and dementia along with involuntary myoclonus and twitches. Some early observations suggest the lack of coordination, loss of balancing capabilities, cognitive dysfunctionality, behavioural flux, depression, mood swings, anxiety, vision impairment and in some rare cases insomnia as early symptoms.Upon progression the intensity of these symptoms worsen and they meld into chaos of variable physical deformities like blindness, loss of speech and locomotion. In extreme cases the immune system gets compromised and this situation subjects the individual to secondary infections (e.g. Pneumonia). Even though it has same progressive neurological symptoms like any another neurological condition, they worsen faster contributing to already established fright.")
            st.write("###")
            st.write("<h3 class='SubHeading-font'> <i><b> Diagnosis </b></i></h3>", unsafe_allow_html=True)
            st.write("Diagnosis can be done using several tests. One of them is Electroencephalography or EEG which records the brain's electrical pattern and finds that peculiar deformity in brain. CSF bases tests are also applicable for such instance where protein testing (respective to a specific area of body) is essential. This testing looks for 14-3-3 protein. It is a marker for some prions. It effectively helps to identify the composition of fluid surrounding the brain and spinal chord. The most successful diagnosis is carried out by MRIs. Brain images obtained from the patient are useful to determine if they have CJD or not. Apart from these methods, confirm diagnosis is only affirmed by brain biopsy or autopsy. In a brain biopsy, a neurosurgeon removes a small piece of tissue from the living person's brain so it can be examined by a neuropathologist. This procedure may be dangerous for the individual and is generally discouraged unless it is needed to rule out a treatable disorder. In an autopsy, the whole brain is examined after death.  Currently there is no cure for CJD, although some drugs are being tested to control it. Today's treatments are aimed at making the person comfortable and easing symptoms. Medications may help relieve pain and muscle jerks. During later stages of the disease, intravenous fluids and machine feeding also may be used.")
            st.write("###")
            st.write("<h3 class='SubHeading-font'> <i><b> Treatment and Management </b></i></h3>", unsafe_allow_html=True)
            st.write("CJD has no definitive treatment, and supportive care is the mainstay of management. Most trial drugs for CJD have not demonstrated any clear benefit to date. However, intraventricular pentosan polysulfate has been shown in rodent studies to inihibit PrPSc formation. An apparent survival extension of 37 to 114 months was observed in four patients.**[2]** More research is needed to find the cure for this fatal condition. Early detection of a PRNP mutation may help families at risk for the genetic form of CJD. Patients affected by the condition can make earlier arrangements for end-of-life concerns. Psychosocial support and supportive care may improve patients' quality of life. Genetic counseling and family planning help prevent disease transmission to the offspring of individuals with PRNP mutation.**[1]**")
            st.write("###")
            st.write("<h3 class='SubHeading-font'> <i><b>Latest Updates</b></i></h3>", unsafe_allow_html=True)
            st.write("Researcher are examining and characterising the prions responsible for this disease. A better understanding of these conditions may enable scientists to acquire some idea over factors that influence the transmission of the disease. Same applies for the parameters of severity.Researchers are investigating the cellular mechanisms involved in abnormal prion formation and accumulation, as well as their replication by select cellular subsets in the brain. Other projects are examining how abnormal prions cross the protective blood-brain barrier and spread throughout the central nervous system, and tests that measure the biological activity of prions. Findings may identify new therapeutic targets to treat prion diseases.")
            st.write("###")
            st.write("<h3 class='SubHeading-font'> <i><b>With The Context of Bioinformatics & Genome Analysis</b></i></h3>", unsafe_allow_html=True)
            st.write("Several bioinformatics analysis techniques are mostly implemented in understanding the key genes which are responsible for underlying side effects of one of the three types of CJDs. One study was aimed to identify key genes and  to understand  underlying neuroinflammation mechanism in sCJD. Several tools were utilised in order to discern the variabilities in  gene expressions and pathway links. GEO dataset (GSE160208) was used to retrieve public data for analysis. WGCNA  was used to identify those key genes by analysing the clusters. Limma R package analysed the differential gene expression to identify  candidates in CJD.  Protein–protein interaction (PPI) network, cytoHubba, and machine learning were used to screen the central genes of SCJD. The chemicals related to hub genes were predicted and explored by molecular docking. 88 candidate genes were screened. Enrichment analysis showed they were mainly related to bacterial and viral infection and immune cell activation. Immune cell infiltration analysis suggested that immune cell activation and altered activity of the immune system are involved in the progression of SCJD. After identifying hub genes, KIT and SPP1 had higher diagnostic efficacy for SCJD (AUC > 0.9), so they were identified as central genes. The molecular docking results showed hub genes both docked well with Tretinoin. KIT, SPP1, and Tretinoin are essential in developing neuroinflammation in SCJD and may provide new ideas for diagnosing and treating SCJD.**[12]**")
            st.write("Another study was carried with an aim to illuminate the underlying molecular mechanisms of sCJD. The mRNA microarray dataset GSE124571 was downloaded from the Gene Expression Omnibus database. Differentially expressed genes (DEGs) were screened. Pathway and GO enrichment analyses of DEGs were performed. PPI network was predicted using  IntAct Molecular Interaction Database and visualised using cytoscope software. Target genes were constructed-miRNA regulatory network and target genes - TF regulatory network. Hub genes were validated. A total of 891 DEGs 448 of these DEGs presented significant up regulated, and the remaining 443 down regulated were obtained. Pathway enrichment analysis indicated that up regulated genes were mainly linked with glutamine degradation/glutamate biosynthesis, while the down regulated genes were involved in melatonin degradation. GO enrichment analyses indicated that up regulated genes were mainly linked with chemical synaptic transmission, while the down regulated genes were involved in regulation of immune system process. **[11]**")

#### REFRENCES ####

if selected == "Related content & Sources":
    #st.title("Related videos")
    st.markdown('<h4 class="Header-font">Related Videos</h4>', unsafe_allow_html=True)
    st.write("###")
    with st.container(border=True):
        l1,r1 = st.columns(2)
        with l1:
            st.image("maxresdefault.jpg", width = 500)
        with r1:
            st.markdown('''<h3 class='SubHeading-font'><i>The Horrifying Science of Prions</i></h3>
                        <h6>This video by YouTube channel named "Dark Science" explains the dangers of prion consumption and how it cause a widespread havoc in UK. Downfall in Biritish political and health-related reliance on government is summerised here.</h6>
                        <a href = "https://youtu.be/zKPuKvZHYPc?feature=shared">Watch</a>''', unsafe_allow_html=True)
            
    st.write("###")
    with st.container(border=True):
        l1,r1 = st.columns(2)
        with l1:
            st.image("hqdefault.jpg", width = 500)
        with r1:
            st.markdown('''<h3 class='SubHeading-font'><i>How Serious is the Threat of Mad Cow Disease?</i></h3>
                        <h6>Three UC Davis agricultural experts debate on the lethal nature of mad cow disease in a discussion sponsored by the Institute of Governmental Affairs</h6>
                        <a href = "https://youtu.be/sMDNORLhYnM?feature=shared">Watch</a>''', unsafe_allow_html=True)
            
    #st.title("References")
    st.markdown("<h3 class='SubHeading-font'>References</h3>",unsafe_allow_html=True)
    st.caption("*Related papers, magazines, books and sites with content regarding :blue[CJD]*")
    st.markdown("""
	
                1. Creutzfeldt-Jakob Disease. (n.d.). National Institute of Neurological Disorders and Stroke. [[NIH](https://www.ninds.nih.gov/health-information/disorders/creutzfeldt-jakob-disease)]
	
                2. Sitammagari, K. K., & Masood, W. (2024, January 30). Creutzfeldt Jakob Disease. StatPearls - [[NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK507860/)]
	
                3. Ishibashi D, Homma T, Nakagaki T, Fuse T, Sano K, Satoh K, Mori T, Atarashi R, Nishida N. Type I interferon protects neurons from prions in in vivo models. Brain. 2019 Apr 01;142(4):1035-1050. [[PMC free article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6439327/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30753318)]. 
	
                4. Gao LP, Shi Q, Xiao K, Wang J, Zhou W, Chen C, Dong XP. The genetic Creutzfeldt-Jakob disease with E200K mutation: analysis of clinical, genetic and laboratory features of 30 Chinese patients. Sci Rep. 2019 Feb 12;9(1):1836. [[PMC free article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6372685/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30755683)]. 
	
                5. Navid J, Day GS, Strain J, Perrin RJ, Bucelli RC, Dincer A, Wisch JK, Soleimani-Meigooni D, Morris JC, Benzinger TLS, Ances BM. Structural signature of sporadic Creutzfeldt-Jakob disease. Eur J Neurol. 2019 Aug;26(8):1037-1043. [[PMC free article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6615963/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30735286)]. 
	
                6. Aslam S, Fritz MA, Cordes L, Sabbagh MN. What Promises the CJD Diagnosis in a Case of Rapidly Progressive Dementia? J Alzheimers Dis Parkinsonism. 2018;8(5) [[PMC free article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6362841/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30733890)] 
	
                7. Johnson RT, Gonzalez RG, Frosch MP. Case records of the Massachusetts General Hospital. Case 27-2005. An 80-year-old man with fatigue, unsteady gait, and confusion. N Engl J Med. 2005 Sep 08;353(10):1042-50. [[PubMed](https://pubmed.ncbi.nlm.nih.gov/16148290)]
	
                8. Ladogana A, Puopolo M, Croes EA, Budka H, Jarius C, Collins S, Klug GM, Sutcliffe T, Giulivi A, Alperovitch A, Delasnerie-Laupretre N, Brandel JP, Poser S, Kretzschmar H, Rietveld I, Mitrova E, Cuesta Jde P, Martinez-Martin P, Glatzel M, Aguzzi A, Knight R, Ward H, Pocchiari M, van Duijn CM, Will RG, Zerr I. Mortality from Creutzfeldt-Jakob disease and related disorders in Europe, Australia, and Canada. Neurology. 2005 May 10;64(9):1586-91. [[PubMed](https://pubmed.ncbi.nlm.nih.gov/15883321)]
	
                9. Klug GM, Wand H, Simpson M, Boyd A, Law M, Masters CL, Matěj R, Howley R, Farrell M, Breithaupt M, Zerr I, van Duijn C, Ibrahim-Verbaas C, Mackenzie J, Will RG, Brandel JP, Alperovitch A, Budka H, Kovacs GG, Jansen GH, Coulthard M, Collins SJ. Intensity of human prion disease surveillance predicts observed disease incidence. J Neurol Neurosurg Psychiatry. 2013 Dec;84(12):1372-7. [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23965290)]
    
                10. Cao, Liming MDa,b,∗; Feng, Hongye BAa,c; Huang, Xuming MAd; Yi, Jiamei BAb; Zhou, Yanxia MAa. Gerstmann-Sträussler-Scheinker syndrome misdiagnosed as cervical spondylotic myelopathy: A case report with 5-year follow-up. Medicine 100(16):p e25687, April 23, 2021. | DOI: 10.1097/MD.0000000000025687 [[Medicine](https://journals.lww.com/md-journal/fulltext/2021/04230/gerstmann_str_ussler_scheinker_syndrome.99.aspx)]
                
                11. Identification of potential key genes and pathway linked with sporadic Creutzfeldt-Jakob disease based on integrated bioinformatics analyses|Basavaraj Vastrad, Chanabasayya Vastrad, Iranna Kotturshetti medRxiv 2020.12.21.20248688; [[Medrxiv](https://doi.org/10.1101/2020.12.21.20248688)]
                
                12. Cheng, Y., Chen, T. & Hu, J. Genetic analysis of potential biomarkers and therapeutic targets in neuroinflammation from sporadic Creutzfeldt–Jakob disease. Sci Rep 13, 14122 (2023). [[Nature](https://doi.org/10.1038/s41598-023-41066-9)]""" ) 
                
    st.write("---")
    with st.container(border=True):
        #st.title("*About*")
        st.markdown("<h3 class='SubHeading-font'>About</h3>",unsafe_allow_html=True)
        st.write("**Developed by:** Jadhav Prathamesh Pradeep Priyanka")
        st.write("**Roll Number:** DY24SBBP0MBI009")
        st.write("**Course:** M.Sc. in Bioinformatics (AY 2024-25)")
        st.write("**Paper:** Introduction to Bioinformatics (Data Mining Assignment)")
        st.markdown("[[Github](https://github.com/Praaathaamesh)]")


with st.container():
    
    st.write("###")
    st.write("###")
    st.write("###")
    st.write("###")
    st.write("###")
st.write("---")
with st.container(border=True):
    st.markdown('''<style>
                "background-color":"hsla(240,92%,5%,1)" 
                </style>
''', unsafe_allow_html=True)
    
    l1,r1 = st.columns(2)
    with l1:
        #st.markdown(''' ### ***“There are no treatments and no cure. These are devastating words for a CJD patient and their families to hear. And while scientists have attempted for decades to understand the mechanisms of prion disease and to identify potential treatments, brain diseases like CJD present special challenges for the research community.”***''')
        st.markdown("<h3 class='SubHeading-font'>“There are no treatments and no cure. These are devastating words for a CJD patient and their families to hear. And while scientists have attempted for decades to understand the mechanisms of prion disease and to identify potential treatments, brain diseases like CJD present special challenges for the research community.</h3>",unsafe_allow_html=True)
        st.caption('*    *-A simplified summary of Dr. Krejciova’s statement in the Concluding Remarks section of the article **"Human stem cell–derived astrocytes replicate human prions in a PRNP genotype–dependent manner"** (Krejciova, Z., et al. The Journal of Experimental Medicine, 2017 Dec 4; 214(12): 3481–3495. doi: 10.1084/jem.20161547ov.), pg. 8*')
    with r1:
        st.markdown("<body><h5 style= 'text-align:center'><i>External Links</i></h5></body>", unsafe_allow_html=True)
        st.caption("*For more information regarding Creutzfeldt-Jakob Disease, visit these external webpages*")
        st.markdown("######")
        st.markdown('''<body>
                    <li> <a href:'https://cjdfoundation.org/'> CJD FOUNDATION</a>
                    <li> <a href:'https://www.ninds.nih.gov/health-information/disorders/creutzfeldt-jakob-disease'> National Institute of Neurological Disorders and Stroke</a>
                    <li> <a href:'https://www.cdc.gov/creutzfeldt-jakob/about/index.html'> Center of Disease Control and Prevention</a>
                    </body>
                    ''', unsafe_allow_html=True)
    
    st.write("####")

footer = """
<style>
a:link, a:visited {
    color: blue;
    background-color: transparent;
    text-decoration: underline;
}

a:hover, a:active {
    color: red;
    background-color: transparent;
    text-decoration: underline;
}

.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #010118;
    color: white;
    text-align: center;
    padding: 10px;
}

.footer p.caption {
    font-size: 12px;  
    color: #cccccc; 
</style>

<div class="footer">
    <p><i>No Copyright Intended</i></p>
    <p class='caption'>Webpage designed as per an assignment activity regarding academic curriculum. No commercial purpose entwined while designing this site. Above content subject towards educational purposes only. Part of Data Mining assignment required for MSCBIP102 (M.Sc. Bioinformatics) (DYPSBB, Navi Mumbai).<br>October-November 2024</p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)