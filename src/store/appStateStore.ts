import { ApplicationsVersions, CriticalProblem, ExternalDependency, NetworkStatus } from '@app/types/app-status';
import { create } from './create';

interface AppState {
    error?: string;
    criticalProblem?: Partial<CriticalProblem>;
    isSettingsOpen: boolean;
    criticalError?: string;
    externalDependencies: ExternalDependency[];
    missingExternalDependencies?: ExternalDependency[];
    issueReference?: string;
    applications_versions?: ApplicationsVersions;
    releaseNotes: string;
    isAppUpdateAvailable: boolean;
    networkStatus?: NetworkStatus;
    isStuckOnOrphanChain: boolean;
}

const initialstate: AppState = {
    isSettingsOpen: false,
    externalDependencies: [],
    missingExternalDependencies: [],
    releaseNotes: '',
    isAppUpdateAvailable: false,
    isStuckOnOrphanChain: false,
};

export const useAppStateStore = create<AppState>()(() => ({
    ...initialstate,
}));
