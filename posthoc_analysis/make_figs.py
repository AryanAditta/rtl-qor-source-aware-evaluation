"""Revised main-text figures, drawn from the frozen per-design data and saved tables (no refitting)."""
import numpy as np, pandas as pd, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os, sys
# Path to the unzipped RTL_QoR_Integration_Final_Review_Package folder (first argument).
P=os.path.join(sys.argv[1] if len(sys.argv)>1 else 'RTL_QoR_Integration_Final_Review_Package',''); FD=P+'figure_data/'; T=P+'tables/'; IN=P+'reproduction/frozen_inputs/m12/inputs/'
O='figures/'; os.makedirs(O,exist_ok=True)
BLUE='#2166AC'; ORANGE='#C65A14'; GREEN='#247B62'; GREY='#707070'; LGREY='#B8B8B8'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.titlesize':9.5,'axes.labelsize':9,
 'xtick.labelsize':8.5,'ytick.labelsize':8.5,'legend.fontsize':8.3,'axes.spines.top':False,
 'axes.spines.right':False,'axes.linewidth':.7,'pdf.fonttype':42,'svg.fonttype':'none',
 'savefig.facecolor':'white','figure.facecolor':'white'})
def save(fig,name):
    for ext in ['png','pdf','svg']: fig.savefig(O+name+'.'+ext,dpi=600 if ext=='png' else None,bbox_inches='tight',pad_inches=.06)
    plt.close(fig)
def panel(ax,l,t): ax.set_title(f'({l}) {t}',loc='left',fontweight='bold',pad=7)
def box(ax,x,y,w,h,text,color=BLUE,fs=8):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012,rounding_size=0.03',fc='white',ec=color,lw=1.15))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs,linespacing=1.35)
def arrow(ax,a,b,color=GREY):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=10,lw=1,color=color))
reserve=pd.read_csv(FD+'reserve_AREA_paired.csv'); source=pd.read_csv(FD+'source50_TIMING_TMIN_paired.csv')
source_area=pd.read_csv(FD+'source50_AREA_paired.csv'); ext=pd.read_csv(FD+'External83_original_points.csv')

# ---------- Fig 2: evaluation roles and counts
fig=plt.figure(figsize=(7.05,4.7)); gs=fig.add_gridspec(2,1,height_ratios=[1.2,1],hspace=.42)
ax=fig.add_subplot(gs[0]); ax.set(xlim=(-.06,10.06),ylim=(0,2.9)); ax.axis('off'); panel(ax,'a','Evaluation cohorts in the order their labels were opened')
box(ax,0,1.55,2.4,.9,'Development corpus\n681 configurations\n498 source components',BLUE,7.2)
box(ax,2.85,1.55,2.3,.9,'Original external test\n83 designs; blind for\nthe native models',BLUE,7.2)
arrow(ax,(2.4,2.0),(2.85,2.0))
box(ax,0,.1,2.4,1.0,'Corpus subsets\nfitting: 538 rows\ncalibration: 143 rows',GREY,7.2)
box(ax,2.85,.1,2.3,1.0,'Fresh Area test\n50 intended designs;\nblind for Area system',GREEN,7.2)
box(ax,5.55,.1,1.95,1.0,'TimingV2 fixed\nafter the Area\ntest was opened',ORANGE,7.0)
box(ax,7.9,.1,2.1,1.0,'Fresh Timing test\n50 intended designs;\nblind for TimingV2',ORANGE,7.2)
arrow(ax,(1.2,1.55),(1.2,1.1)); arrow(ax,(2.4,.6),(2.85,.6)); arrow(ax,(5.15,.6),(5.55,.6)); arrow(ax,(7.5,.6),(7.9,.6))
ax.text(5.55,1.62,'A cohort is fresh only for the model that was\nfrozen before its labels were opened. Later\nmodels evaluated on it are retrospective.',fontsize=7.6,linespacing=1.45,va='bottom')
ax=fig.add_subplot(gs[1]); panel(ax,'b','Intended, predicted, labelled and paired designs (separate sets)')
names=['Original external test','Fresh Area test','Fresh Timing test']; vals=np.array([[100,100,83,83],[50,47,40,39],[50,41,45,39]])
x=np.arange(3); w=.19
for j,(lab,col,h) in enumerate(zip(['Intended','Prediction available','Valid physical label','Paired (both)'],[LGREY,BLUE,ORANGE,GREEN],['','//','..','xx'])):
    b=ax.bar(x+(j-1.5)*w,vals[:,j],w,color=col,hatch=h,edgecolor='white',lw=.4,label=lab); ax.bar_label(b,padding=2,fontsize=7.8)
ax.set(xticks=x,xticklabels=names,ylim=(0,122),ylabel='Designs'); ax.grid(axis='y',ls=':',lw=.6,alpha=.4)
ax.legend(ncol=4,frameon=False,loc='upper center',bbox_to_anchor=(.5,-.17),fontsize=7.8)
save(fig,'Fig02')

# ---------- Fig 3: per-design predictions
fig,axs=plt.subplots(2,2,figsize=(7.05,6.0),layout='constrained')
for ax,l,t,y,p,c,u in [(axs[0,0],'a','External test: Area (original native)',ext.actual_area_um2,ext.area_prediction_um2,BLUE,'µm²'),
 (axs[0,1],'b','External test: Tmin (original native)',ext.actual_tmin_ns,ext.timing_tmin_prediction_ns,BLUE,'ns'),
 (axs[1,0],'c','Fresh Area test: Area system',reserve.measured,reserve.candidate,GREEN,'µm²'),
 (axs[1,1],'d','Fresh Timing test: TimingV2',source.measured,source.candidate,ORANGE,'ns')]:
    y=np.asarray(y,float);p=np.asarray(p,float); assert ((y>0)&(p>0)).all()
    lo=min(y.min(),p.min())*.65;hi=max(y.max(),p.max())*1.55;xx=np.geomspace(lo,hi,200)
    ax.fill_between(xx,xx/1.25,xx*1.25,color='#DCE9E3',zorder=0); ax.plot(xx,xx,'--',color=GREY,lw=.9)
    ax.scatter(y,p,s=20,color=c,alpha=.8,edgecolors='white',linewidth=.35)
    ax.set(xscale='log',yscale='log',xlim=(lo,hi),ylim=(lo,hi),xlabel=f'Measured ({u})',ylabel=f'Predicted ({u})')
    ax.set_aspect('equal'); panel(ax,l,t); ax.text(.05,.94,f'n = {len(y)}',transform=ax.transAxes,va='top',fontsize=8.5)
    ax.grid(ls=':',lw=.5,alpha=.4)
    if l=='b':
        i=np.flatnonzero(ext.top_module.eq('pipelineTop'))[0]
        ax.annotate('pipelineTop',xy=(y[i],p[i]),xytext=(.18,.75),textcoords='axes fraction',fontsize=8,arrowprops=dict(arrowstyle='->',color=GREY,lw=.8))
save(fig,'Fig03')

# ---------- Fig 4: paired per-design errors and saved contrasts
fig,axs=plt.subplots(2,2,figsize=(7.05,5.0),gridspec_kw={'width_ratios':[1.3,1]},layout='constrained')
for row,d,t,c,dl,lo,hi in [(0,reserve,'Fresh Area test: Area system vs native',GREEN,-.311442,-.504499,-.142821),
                           (1,source,'Fresh Timing test: TimingV2 vs native',ORANGE,-.0165457,-.0284220,-.00497390)]:
    ax=axs[row,0];xx=d.native_abs_log1p_error;yy=d.candidate_abs_log1p_error;lim=max(xx.max(),yy.max())*1.08
    ax.plot([0,lim],[0,lim],'--',color=GREY,lw=.8);ax.scatter(xx,yy,c=c,s=23,alpha=.85,edgecolors='white',linewidth=.3)
    ax.set(xlim=(0,lim),ylim=(0,lim),xlabel='Native reference error',ylabel='Candidate error')
    nb=(yy<xx).sum(); panel(ax,'ac'[row],t); ax.text(.04,.93,f'{nb} lower · {39-nb} higher (of 39)\nbelow the line favours the candidate',transform=ax.transAxes,va='top',fontsize=8)
    ax.grid(ls=':',lw=.5,alpha=.4)
    ax=axs[row,1];ax.axvline(0,color=GREY,ls='--',lw=.8)
    ax.errorbar(dl,0,xerr=[[dl-lo],[hi-dl]],fmt='D',ms=6,color=c,capsize=4,lw=1.5)
    ax.set(ylim=(-.8,.8),yticks=[],xlabel='Candidate − native (macro error)'); ax.set_xlim(lo*1.2,abs(lo)*.18)
    panel(ax,'bd'[row],'Paired difference, 95% CI'); ax.text(.03,.93,f'Δ = {dl:.4f}\n[{lo:.4f}, {hi:.4f}]',transform=ax.transAxes,va='top',fontsize=8.5)
save(fig,'Fig04')

# ---------- Fig 5: development to fresh evaluation
area=[('Fitting subset, development\n(538 rows, 398 comp.)',.425823,.370183,None,None,'dev'),
      ('Graph-supported subset, development\n(168 rows, 166 comp.)',.362593,.229191,None,None,'dev'),
      ('Fresh Area test, primary\n(39 paired)',.528360,.216918,-.504499,-.142821,'fresh'),
      ('Fresh Timing test, secondary Area\n(39 paired)',.465346,.170802,None,None,'fresh2')]
tim=[('Fitting subset, development\n(538 rows, 398 comp.)',.133929,.122494,None,None,'dev'),
     ('Calibration subset, held out\n(143 rows, 100 comp.)',.125774,.113848,None,None,'dev'),
     ('Fresh Area test, retrospective\n(39 paired)',.152187,.135660,-.0590671,.0209740,'retro'),
     ('Fresh Timing test, primary\n(39 paired)',.0945522,.0780065,-.0284220,-.00497390,'fresh')]
fig,axs=plt.subplots(2,1,figsize=(7.05,5.4)); fig.subplots_adjust(left=.30,right=.70,top=.9,bottom=.09,hspace=.55)
for ax,rows,c,l,t,xl in [(axs[0],area,GREEN,'a','Area: native reference vs Area system',(0,.6)),(axs[1],tim,ORANGE,'b','Tmin: native reference vs TimingV2',(0,.17))]:
    ys=np.arange(len(rows))[::-1]
    for y,(name,r,cand,lo,hi,kind) in zip(ys,rows):
        ax.plot([cand,r],[y,y],color=LGREY,lw=2.2,zorder=1)
        ax.scatter(r,y,s=38,color=GREY,zorder=2,label='Native reference' if y==ys[0] else None)
        ax.scatter(cand,y,s=42,color=c,zorder=3,marker='D',label='Candidate' if y==ys[0] else None)
        txt=f'{100*(1-cand/r):.1f}% lower'
        txt+=(f'\nΔ 95% CI [{lo:.3f}, {hi:.3f}]' if lo is not None else '')
        ax.text(1.03,y,txt,transform=ax.get_yaxis_transform(),ha='left',va='center',fontsize=7.5,color=GREY if kind=='retro' else 'black',clip_on=False)
    ax.set(yticks=ys,yticklabels=[r[0] for r in rows],xlim=xl,ylim=(-.6,len(rows)-.4),xlabel='Component-macro absolute log1p error')
    ax.tick_params(axis='y',labelsize=7.6); ax.grid(axis='x',ls=':',lw=.5,alpha=.5); panel(ax,l,t)
axs[0].legend(frameon=False,loc='lower left',ncol=2,fontsize=7.8,bbox_to_anchor=(-.02,1.1))
save(fig,'Fig05')

# ---------- Fig 6: size controls
size=pd.read_csv(FD+'Size_controls.csv')
fig,axs=plt.subplots(1,2,figsize=(7.05,2.9),layout='constrained')
for ax,tg,l,t in [(axs[0],'AREA','a','Area'),(axs[1],'TIMING_TMIN','b','Tmin')]:
    pops=['Full681','External83']; plabs=['Development (OOF)','External test']; w=.25; x=np.arange(2)
    for j,(m,col,h,lab) in enumerate([('SIZE_1',LGREY,'//','Cell count'),('SIZE_2','#8F8F8F','..','Cell count + sequential bits'),('NATIVE',BLUE,'','Native structural model')]):
        v=[]
        for p in pops:
            a=size[(size.Target==tg)&(size.Population==p)]
            v.append(float((a[a.Method==m] if m!='NATIVE' else a[~a.Method.isin(['SIZE_1','SIZE_2'])])['Macro log error'].iloc[0]))
        b=ax.bar(x+(j-1)*w,v,w,color=col,hatch=h,edgecolor='black',lw=.4,label=lab); ax.bar_label(b,fmt='%.3f',padding=2,fontsize=7.6)
    ax.set(xticks=x,xticklabels=plabs,ylabel='Macro log1p error'); ax.set_ylim(0,ax.get_ylim()[1]*1.12); panel(ax,l,t); ax.grid(axis='y',ls=':',lw=.5,alpha=.4)
fig.legend(*axs[0].get_legend_handles_labels(),frameon=False,fontsize=7.8,loc='lower center',ncol=3,bbox_to_anchor=(.5,-.09))
save(fig,'Fig06')

# ---------- Fig 7: family ablation
a=pd.read_csv(T+'M13_PAIRED_DELTAS.csv'); fig,ax=plt.subplots(figsize=(7.05,3.5),layout='constrained')
env=float(a.N_seed.iloc[0]); ax.axvspan(-env,env,color='#E4E4E4',label='Seed-to-seed range of the full model'); ax.axvline(0,color=GREY,ls='--',lw=.8)
ys=np.arange(len(a))[::-1]
for y,(_,r) in zip(ys,a.iterrows()):
    m=r.mean_component_delta_minus_full
    ax.errorbar(m,y,xerr=[[m-r.descriptive_CI95_lower],[r.descriptive_CI95_upper-m]],fmt='o',color=ORANGE if r.family_id=='F1' else BLUE,capsize=3,ms=4.5,lw=1.1)
ax.set(yticks=ys,yticklabels=[f'{r.family_id}  {r.family} ({r.removed_features})' for _,r in a.iterrows()],xlabel='Error after removing family − full-model error (macro log1p)',xlim=(-.0055,.0295))
ax.legend(frameon=False,loc='lower right'); ax.grid(axis='x',ls=':',lw=.5)
save(fig,'Fig07')

# ---------- Fig 8: interval coverage and relative width
iv=pd.read_csv('PH2_relative_interval_widths.csv')
order=['Fresh Area test, Area system','Fresh Area test, native Area reference','Fresh Timing test, TimingV2','Fresh Timing test, native Timing reference']
labs=['Fresh Area test\nArea system','Fresh Area test\nnative reference†','Fresh Timing test\nTimingV2','Fresh Timing test\nnative reference']
iv=iv.set_index('interval').loc[order]; cols=[GREEN,GREY,ORANGE,GREY]
fig,axs=plt.subplots(1,2,figsize=(7.05,2.9),layout='constrained',gridspec_kw={'width_ratios':[1.15,1]})
y=np.arange(4)[::-1]; ax=axs[0]; ax.axvline(90,color=GREY,ls='--',lw=.8)
cov=iv.covered/iv.n*100; ax.scatter(cov,y,c=cols,s=34)
for yi,(k,r) in zip(y,iv.iterrows()): ax.annotate(f'{int(r.covered)}/{int(r.n)}',(r.covered/r.n*100,yi),xytext=(0,7),textcoords='offset points',ha='center',fontsize=8)
ax.set(yticks=y,yticklabels=labs,xlim=(80,104),ylim=(-.6,3.7),xlabel='Observed coverage (%), nominal 90%'); ax.tick_params(axis='y',labelsize=7.8); panel(ax,'a','Coverage')
ax.grid(axis='x',ls=':',lw=.5)
ax=axs[1]; ax.barh(y,iv.median_rel_width,color=cols,height=.5)
for yi,v in zip(y,iv.median_rel_width): ax.text(v+.05,yi,f'{v:.2f}×',va='center',fontsize=8)
ax.set(yticks=y,yticklabels=[],xlim=(0,3.6),ylim=(-.6,3.7),xlabel='Median interval width ÷ point prediction'); panel(ax,'b','Relative width'); ax.grid(axis='x',ls=':',lw=.5)
save(fig,'Fig08')
print('ok')
