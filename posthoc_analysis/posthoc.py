"""Post-hoc robustness analyses on frozen per-design predictions (no refitting)."""
import pandas as pd, numpy as np, json, sys
import os, sys
# Path to the unzipped RTL_QoR_Integration_Final_Review_Package folder (first argument).
P=os.path.join(sys.argv[1] if len(sys.argv)>1 else 'RTL_QoR_Integration_Final_Review_Package','')
FD=P+'figure_data/'; IN=P+'reproduction/frozen_inputs/m12/inputs/'
rng_seed=20261020; B=5000
out={}
def boot(diff,seed):
    r=np.random.default_rng(seed); n=len(diff)
    m=np.array([diff[r.integers(0,n,n)].mean() for _ in range(B)])
    return np.percentile(m,[2.5,97.5])
rows=[]
for name,f,unit in [('Fresh Area test (Reserve50) - primary','reserve_AREA_paired','um2'),
                    ('Fresh Timing test (Source50) - primary','source50_TIMING_TMIN_paired','ns'),
                    ('Fresh Timing test (Source50) - secondary Area','source50_AREA_paired','um2')]:
    d=pd.read_csv(FD+f+'.csv'); y=d.measured.values; c=d.candidate.values; n=d.native.values
    assert (y>0).all() and (c>0).all() and (n>0).all()
    lc=np.abs(np.log(c/y)); ln=np.abs(np.log(n/y)); diff=lc-ln
    lo,hi=boot(diff,rng_seed)
    # sign agreement with primary loss
    prim=d.candidate_abs_log1p_error.values-d.native_abs_log1p_error.values
    rows.append(dict(endpoint=name,n=len(d),
      native_mean_abs_log_ratio=ln.mean(),candidate_mean_abs_log_ratio=lc.mean(),
      reduction_pct=100*(1-lc.mean()/ln.mean()),delta=diff.mean(),ci_lo=lo,ci_hi=hi,
      improved=(diff<0).sum(),
      native_median_factor=np.exp(np.median(ln)),candidate_median_factor=np.exp(np.median(lc)),
      native_within_1_25x=(ln<=np.log(1.25)).sum(),candidate_within_1_25x=(lc<=np.log(1.25)).sum(),
      native_within_2x=(ln<=np.log(2)).sum(),candidate_within_2x=(lc<=np.log(2)).sum(),
      sign_agreement_with_primary=int((np.sign(diff)==np.sign(prim)).sum())))
lr=pd.DataFrame(rows); print(lr.T.to_string())
lr.to_csv('PH1_log_ratio_contrasts.csv',index=False)

# Relative interval widths (width divided by point prediction), nominal 90%
def relw(pred,lo,hi,y):
    pred=np.asarray(pred,float);lo=np.asarray(lo,float);hi=np.asarray(hi,float);y=np.asarray(y,float)
    cov=((y>=lo)&(y<=hi)).sum()
    return dict(n=len(y),covered=int(cov),median_abs_width=np.median(hi-lo),median_rel_width=np.median((hi-lo)/pred),
                median_upper_over_pred=np.median(hi/pred),lower_at_zero=int((lo<=0).sum()),
                median_measured=np.median(y))
iv=[]
r=pd.read_csv(FD+'reserve_AREA_paired.csv'); iv.append(dict(interval='Fresh Area test, Area system',**relw(r.candidate,r.lower,r.upper,r.measured)))
rn=pd.read_csv(IN+'reserve_native.csv').set_index('request_id').loc[r.request_id]
iv.append(dict(interval='Fresh Area test, native Area reference',**relw(rn.AREA_prediction,rn.AREA_lower,rn.AREA_upper,r.measured.values)))
s=pd.read_csv(FD+'source50_TIMING_TMIN_paired.csv'); iv.append(dict(interval='Fresh Timing test, TimingV2',**relw(s.candidate,s.lower,s.upper,s.measured)))
sn=pd.read_csv(IN+'source50_native.csv').set_index('request_id').loc[s.request_id]
iv.append(dict(interval='Fresh Timing test, native Timing reference',**relw(sn.TIMING_TMIN_prediction,sn.TIMING_TMIN_lower,sn.TIMING_TMIN_upper,s.measured.values)))
sa=pd.read_csv(FD+'source50_AREA_paired.csv'); iv.append(dict(interval='Fresh Timing test, secondary Area system',**relw(sa.candidate,sa.lower,sa.upper,sa.measured)))
san=pd.read_csv(IN+'source50_native.csv').set_index('request_id').loc[sa.request_id]
iv.append(dict(interval='Fresh Timing test, secondary native Area',**relw(san.AREA_prediction,san.AREA_lower,san.AREA_upper,sa.measured.values)))
ivd=pd.DataFrame(iv); print(ivd.to_string()); ivd.to_csv('PH2_relative_interval_widths.csv',index=False)

# Paired absolute-error (physical units) contrasts, same bootstrap settings
ae=[]
for name,f in [('Fresh Area test - Area','reserve_AREA_paired'),('Fresh Timing test - Timing','source50_TIMING_TMIN_paired'),('Fresh Timing test - secondary Area','source50_AREA_paired')]:
    d=pd.read_csv(FD+f+'.csv'); diff=np.abs(d.candidate-d.measured).values-np.abs(d.native-d.measured).values
    lo,hi=boot(diff,rng_seed)
    # median-of-differences
    ae.append(dict(endpoint=name,native_MAE=np.abs(d.native-d.measured).mean(),candidate_MAE=np.abs(d.candidate-d.measured).mean(),delta=diff.mean(),ci_lo=lo,ci_hi=hi,improved=int((diff<0).sum())))
aed=pd.DataFrame(ae); print(aed.to_string()); aed.to_csv('PH3_absolute_error_contrasts.csv',index=False)
# Where does Timing log-ratio disagreement come from? small-Tmin designs
d=pd.read_csv(FD+'source50_TIMING_TMIN_paired.csv'); 
d['dlr']=np.abs(np.log(d.candidate/d.measured))-np.abs(np.log(d.native/d.measured))
print(d.sort_values('measured')[['measured','native','candidate','dlr']].head(8).to_string())
print('small (<0.2ns) n',(d.measured<0.2).sum(),'sum dlr small',d.dlr[d.measured<0.2].sum(),'sum dlr rest',d.dlr[d.measured>=0.2].sum())
