# Code from my Stack Overflow answer https://stackoverflow.com/a/75636599 (posted 2023-03-04), extracted verbatim; may need the question's context to run.
cashflows_df = pd.DataFrame([{'Ticket': tId, **{
    k: v for k, v in cfd.items() if k != 'TicketId'
}} for tId, cf in zip(
    # tickets_df['TicketId'], tickets_df['CashFlows']
    tickets_df.index, tickets_df['CashFlows'] # if TicketId is the index
) for cfd in cf['CashFlowDto']])
