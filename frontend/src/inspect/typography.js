const baselines=new WeakMap();
/** Read all baselines before writing any descendant to avoid nested scaling. */
export function scaleTypography(panel,scale=1) {
  const elements=[panel,...panel.querySelectorAll('*')];
  // Newly inserted children must inherit the unscaled parent baseline.
  // All restoration/measurement/writes happen in this task before paint.
  elements.forEach(element=>{if(baselines.has(element))element.style.fontSize=`${baselines.get(element)}px`;});
  const sizes=elements.map(element=>{
    if(!baselines.has(element))baselines.set(element,parseFloat(getComputedStyle(element).fontSize));
    return baselines.get(element);
  });
  elements.forEach((element,index)=>{if(Number.isFinite(sizes[index]))element.style.fontSize=`${sizes[index]*scale}px`;});
}
