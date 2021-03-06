import awkward
import numpy
import numba 

import selections.selection_utils as utils
import selections.object_selections as object_selections

def select_jets(events, photons, electrons, muons, taus, jets, options, debug):
    cut_diagnostics = utils.ObjectCutDiagnostics(objects = jets, cut_set = "[jet_selections.py : select_jets]", debug = debug)

    pt_cut = jets.pt > options["jets"]["pt"]
    eta_cut = abs(jets.eta) < options["jets"]["eta"]

    dR_pho_cut = object_selections.select_deltaR(events, jets, photons, options["jets"]["dR_pho"], debug)
    dR_ele_cut = object_selections.select_deltaR(events, jets, electrons, options["jets"]["dR_lep"], debug)
    dR_muon_cut = object_selections.select_deltaR(events, jets, muons, options["jets"]["dR_lep"], debug)

    if taus is not None:
        dR_tau_cut = object_selections.select_deltaR(events, jets, taus, options["jets"]["dR_tau"], debug)
    else:
        dR_tau_cut = object_selections.select_deltaR(events, jets, photons, 0.0, debug) # dummy cut of all True

    jet_cut = pt_cut & eta_cut & dR_pho_cut & dR_ele_cut & dR_muon_cut & dR_tau_cut

    cut_diagnostics.add_cuts([pt_cut, eta_cut, dR_pho_cut, dR_ele_cut, dR_muon_cut, dR_tau_cut, jet_cut], ["pt > 25", "|eta| < 2.4", "dR_photons", "dR_electrons", "dR_muons", "dR_taus", "all"])
    
    return jet_cut

def set_jets(events, jets, options, debug):
    events["n_jets"] = awkward.num(jets)

    n_save = options["jets"]["n_jets_save"]
    jet_pt_padded = utils.pad_awkward_array(jets.pt, n_save, -9)
    jet_eta_padded = utils.pad_awkward_array(jets.eta, n_save, -9)
    jet_id_padded = utils.pad_awkward_array(jets.jetId, n_save, -9)
    jet_btagDeepFlavB_padded = utils.pad_awkward_array(jets.btagDeepFlavB, n_save, -9)

    for i in range(n_save):
        events["jet%s_pt" % str(i+1)] = jet_pt_padded[:,i]
        events["jet%s_eta" % str(i+1)] = jet_eta_padded[:,i]
        events["jet%s_id" % str(i+1)] = jet_id_padded[:,i]
        events["jet%s_bTagDeepFlavB" % str(i+1)] = jet_btagDeepFlavB_padded[:,i]

    return events
